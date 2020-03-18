FROM ros:eloquent-ros-core

RUN apt-get update && apt-get install -y --no-install-recommends \
	ros-${ROS_DISTRO}-tf2-ros \
	&& rm -rf /var/lib/apt/lists/*

COPY . /src

RUN cd /src && colcon build

RUN echo '#!/usr/bin/env sh \n\    
    . /opt/ros/${ROS_DISTRO}/setup.sh \n\    
    . /src/install/setup.sh \n' >> /entrypoint.sh && \    
    echo 'exec "$@"' >> /entrypoint.sh && chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
