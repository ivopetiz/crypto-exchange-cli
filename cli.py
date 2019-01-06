#!/usr/bin/python2.7

import sys
import time

from poloniex import Poloniex

pl = Poloniex()

# 1m  |  5m  | 10m  | 20m | 30m  |  1h |  3h  |  6h  | 12h  | 24h  |  Price  |Volume
x = [0, 1, 2, 4, 6, 12, 36, 72, 144, 288]

# get_volumes returns volumes from X different coins.
def get_volumes():
	cur_print = []
	btc_price = get_btc_price()
	try:
		Volumes = pl.return24hVolume()
	except:
		return 1
	for i in Volumes:
		if "USDT_" in i:
			cur_print.append((i,int(float(Volumes[i]['USDT']))))
		if "BTC_" in i:
			cur_print.append((i,int(float(Volumes[i]['BTC']))*btc_price))
	cur_print.sort(key=lambda tup:tup[1], reverse=True)
	if len(sys.argv)>1:
		results=int(sys.argv[1])
	else:
		results = 30
			
	return cur_print[0:results]


# get_btc_price returns BTC price in USDT.
def get_btc_price():
	return float(pl.returnTicker()['USDT_BTC']['last'])


# get_indicator returns a symbol, indicating if price is going up or down,
#  according to simple moving average. SHOULDN'T BE TAKEN TOO SERIOUS!

def get_indicator(d):
	# not used yet.
	if sideways:
		return '\u219D'
	if sell:
		return '\u2198'
	if buy:
		return '\u2197'


def var(list_):
	val_list = []
	for i in range(1,len(x)):
		val = round(float(list_[x[i-1]]*100/list_[x[i]])-100, 2)
		val_list.append(add_color(val))
	val_list.append(add_color(round(float(list_[0]*100/list_[x[-1]-1])-100, 2)))
	return val_list


# add_color adds color to CLI, according to price variation.	
def add_color(val):
	if val < -3 or val >3:
		factor = '7'
	else:
		factor = '1'
	#'\033[1;32m
	if val > 0:
		val = '\033[{};32m{:^6}\033[0;m'.format(factor,str(val))
		#color = 'green'
	elif val < 0:
		val = '\033[{};31m{:^6}\033[0;m'.format(factor,str(val))
		#color = 'red'
	else:
		val = '\033[{};30m{:^6}\033[0;m'.format('1','0.0')
	return val

# print_head plots first line of CLI.
def print_head():
	print '{:^10}|{:^6}|{:^6}|{:^6}|{:^6}|{:^6}|{:^6}|{:^6}|{:^6}|{:^6}|{:^6}|{:^10}|{:^8}'\
			.format('Pair','1m','5m','10m','20m','30m',
				'1h','3h','6h','12h','24h', 'Price','Volume')
	print ' {}+{}+{}+{}+{}+{}+{}+{}+{}+{}+{}+{}+{}'\
			.format('-'*9,'-'*6,'-'*6,'-'*6,'-'*6,'-'*6,
					'-'*6,'-'*6,'-'*6,'-'*6,'-'*6,'-'*10,'-'*8)

# main
def main():
	if len(sys.argv)==1:
		stop = 30
	else:
		if ('--nocolor' or '-c') in sys.argv:
			nocolor = True
#		if ('--mycoins' or '-m') in sys.argv:

	if len(sys.argv)>1:
		stop = int(sys.argv[1])
	else:
		stop = 30

	print "\033c"
	print_head()
	
	while(1):
		try:
			currencies = get_volumes()
			for currency in currencies:
				if currency[1] > 200000:
					a = [float(item['weightedAverage']) for item in pl.returnChartData(currency[0],300)]
					val_list = var(list(reversed(a)))
					if a[-1]>1:
						price_val = "%.4f" % a[-1]
					else:
						price_val = "%.8f" % a[-1]
					print '{:^10}|{:^6}|{:^6}|{:^6}|{:^6}|{:^6}|{:^6}|{:^6}|{:^6}|{:^6}|{:^6}|{:^10}|{:>6}'\
						.format(currency[0], val_list[0], val_list[1], val_list[2], val_list[3],
							val_list[4], val_list[5], val_list[6], val_list[7], val_list[8],
                    	    val_list[9], price_val, str(int(currency[1]/1000000)) + ' M')
			old_currencies = currencies
		except Exception as e:
			print "\033c"
			print "Error getting data."

		time.sleep(60 - stop)

		print "\033c"
		print_head()

if __name__=="__main__":
	main()
