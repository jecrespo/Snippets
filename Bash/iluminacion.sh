#!/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
DAEMON=php -f /var/www/iluminacion/conectabdd.php
DAEMON_OPTS='opciones'
NAME=iluminacion
DESC=proceso que arranca la supervision de la iluminacion
PIDFILE="/var/run/${NAME}.pid"
QUIET="--quiet"
START_OPTS="--start ${QUIET} --background --make-pidfile --pidfile ${PIDFILE} --exec ${DAEMON} ${DAEMON_OPTS}"
STOP_OPTS="--stop --pidfile ${PIDFILE}"
OWNER=root
LOGDIR=/var/log/${NAME}

test -x $DAEMON || exit 0

# SI NO EXISTE EL DIRECTORIO LOG, LOS CREAMOS
if [ ! -d "$LOGDIR" ]; then
    mkdir -m 750 $LOGDIR
    chown $OWNER:$OWNER $LOGDIR
fi

set -e

case "$1" in
  start)
	echo -n "Starting $DESC: "
	start-stop-daemon $START_OPTS
	echo "$NAME."
	;;
  stop)
	echo -n "Stopping $DESC: "
	start-stop-daemon $STOP_OPTS
	echo "$NAME."
        rm $PIDFILE
	;;
  restart|force-reload)
	echo -n "Restarting $DESC: "
	start-stop-daemon $STOP_OPTS
	sleep 1
	start-stop-daemon $START_OPTS
	echo "$NAME."
	;;
  *)
	N=/etc/init.d/$NAME
	echo "Usage: $N {start|stop|restart|force-reload}" >&2
	exit 1
	;;
esac

exit 0