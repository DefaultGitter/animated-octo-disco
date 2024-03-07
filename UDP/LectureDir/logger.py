import logging

# logging.basicConfig(level=logging.DEBUG, filename='mylog.log', filemode='w',
logging.basicConfig(level=logging.WARNING, filename='mylog.log', filemode='w',
                    format='%(asctime)s %(levelname)s - %(message)s')
# format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical hint')
