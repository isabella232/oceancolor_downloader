from datetime import datetime
import urllib
import bz2
from osgeo import gdal
from osgeo import osr
import numpy as np
import ocfiledates
from dateutil.relativedelta import relativedelta

class Chl:
	"""
	This is my CHL class
	"""

	def __init__(self, start_date, end_date, res, time_composite='Annual'):
		
		self.start_date     = start_date
		self.end_date       = end_date
		self.res            = res
		self.time_composite = time_composite

		if self.res == 4:
			self.geo = [-180.0, 0.04166666791, 0.0, 90.0, 0.0, -0.04166666791]
		elif self.res == 9:
			self.geo = [-180.0, 0.08333333582, 0.0, 90.0, 0.0, -0.08333333582]

    		self.outproj = osr.SpatialReference()
    		self.outproj.SetWellKnownGeogCS("WGS84")    
    		self.nodata = -32767


	def download(self, path):
		"""
		This downloads
	
		"""
		self.path = path
		filenames = self.__createfilenames()
		for f in filenames:
			f_uncompress = self.__extract(f)
			self.__process(f_uncompress)


	def __createfilenames(self):
		"""
		Creates a list of filenames based on inputs 
		"""
		minyear = self.start_date.year
		maxyear = self.end_date.year

		leap_years = [x for x in range(minyear, maxyear+1) 
			if (x % 400 == 0) or (x % 4 == 0 and not x % 100 == 0)]
	
		filenames = []
		if self.time_composite == 'Annual':

			minyear = self.start_date.year
			maxyear = self.end_date.year

			for year in range(minyear, maxyear + 1):
				if year in leap_years:
					filenames.append('A{0}001{0}366.L3m_YR_CHL_chlor_a_{1}km'.format(year, self.res))
				else:
					filenames.append('A{0}001{0}365.L3m_YR_CHL_chlor_a_{1}km'.format(year, self.res))
		
		if self.time_composite == 'Monthly':
			d = self.start_date
			while d <= self.end_date:
				m = d.month
				if d.year in leap_years:
					date_ref = ocfiledates.monthly_leap
				else:
					date_ref = ocfiledates.monthly_nonleap
				filenames.append('A{0}{1}{0}{2}.L3m_MO_CHL_chlor_a_{3}km'.format(d.year, date_ref[m][0], date_ref[m][1], self.res))
				d = d + relativedelta(months=1)

		if self.time_composite == 'Daily':
			d = self.start_date
			while d <= self.end_date:
				doy = d.strftime('%j')
				filenames.append('A{0}{1}.L3m_DAY_CHL_chlor_a_{2}km'.format(d.year, doy, self.res))
				d = d + relativedelta(days=1)
		
		if self.time_composite == '8 day':
			d = self.start_date
			print d
			doy = d.strftime('%j')
			print doy
			date_ref = ocfiledates.wk
			#get it so the date is at the start of any 8 day period to initialise the loop
			for dr in date_ref:
				if int(doy) in dr:
					doy = min(dr)
					d = datetime.strptime('{} {}'.format(d.year, doy), '%Y %j')
			while d <= self.end_date:
				doy = d.strftime('%j')
				if d.year in leap_years:
					date_ref = ocfiledates.wk_leap
					mindoy = int(doy)
					maxdoy = max(date_ref[mindoy])
					filenames.append('A{0}{1:0>3}{0}{2:0>3}.L3m_8D_CHL_chlor_a_{3}km'.format(d.year, mindoy, maxdoy, self.res))
					if mindoy == 361:
						d = d + relativedelta(days=6)
					else:
						d = d + relativedelta(days=8)
				else:

					date_ref = ocfiledates.wk_nonleap
					mindoy = int(doy)
					print 'mindoy', mindoy
					maxdoy = max(date_ref[mindoy])
					filenames.append('A{0}{1:0>3}{0}{2:0>3}.L3m_8D_CHL_chlor_a_{3}km'.format(d.year, mindoy, maxdoy, self.res))
					if mindoy == 361:
						d = d + relativedelta(days=5)
					else:
						d = d + relativedelta(days=8)
		
		return filenames


	def __extract(self, targetfile):
		"""
		Private method to download and extract a file 
		"""

		f_download = 'http://oceandata.sci.gsfc.nasa.gov/cgi/getfile/{}.bz2'.format(targetfile)
		f_compress = '{0}{1}.bz2'.format(self.path, targetfile)
		f_uncompress = '{0}{1}'.format(self.path, targetfile)
		urllib.urlretrieve(f_download, f_compress)
		uncom = bz2.BZ2File(f_compress, 'r').read()
		output = open(f_uncompress, 'w')
		output.write(uncom)
		output.close()

		return f_uncompress


	def __process(self, targetfile):
		"""
		This processes the uncompressed file downloaded 
		in self.__extract()
		"""
		outname = '{0}.tif'.format(targetfile)
		g = gdal.Open(targetfile)
		
		arr = g.ReadAsArray()
		arr = np.array(arr)
		[cols, rows] = arr.shape
		
		outdata = gdal.GetDriverByName("GTiff")
		
		dst_ds = outdata.Create(outname, rows, cols, 1, gdal.GDT_Float32)
		
		band = dst_ds.GetRasterBand(1)
		band.SetNoDataValue(self.nodata)
		dst_ds.SetGeoTransform(self.geo)
		dst_ds.SetProjection(self.outproj.ExportToWkt())
		dst_ds.SetMetadataItem('SENSOR', 'AQUA_MODIS')
		dst_ds.SetMetadataItem('RESOLUTION', '{}km'.format(self.res))
		dst_ds.SetMetadataItem('DATA START DAY', g.GetMetadataItem('Period Start Day'))
		dst_ds.SetMetadataItem('DATA END DAY', g.GetMetadataItem('Period End Day'))
		dst_ds.SetMetadataItem('DATA START YEAR', g.GetMetadataItem('Period Start Year'))
		dst_ds.SetMetadataItem('DATA END YEAR', g.GetMetadataItem('Period End Year'))
		date = datetime.now()
		date = date.strftime('%Y-%m-%d')
		dst_ds.SetMetadataItem('DOWNLOAD_DATE', date)
		dst_ds.SetMetadataItem('DOWNLOAD_FROM', 'NASA OCEANCOLOUR')
		dst_ds.SetMetadataItem('PRODUCT_NAME', targetfile)
		dst_ds.SetMetadataItem('PARAMETER', g.GetMetadataItem('Parameter'))
		dst_ds.SetMetadataItem('UNITS', g.GetMetadataItem('Units'))
		dst_ds.SetMetadataItem('NODATA VALUE', '{}'.format(self.nodata))
		dst_ds.SetMetadataItem('YEAR', g.GetMetadataItem('Start Year'))
		band.WriteArray(arr)


if __name__ == "__main__":
	sd = datetime(2004, 12, 01)
	ed = datetime(2005, 12, 15)
	d = Chl(sd, ed, 9, '8 day')
	d.download('/Users/Ireland/rsr/qgis-dev/test_8day/')

