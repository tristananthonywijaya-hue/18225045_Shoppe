from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='18225045_Shopee',
            executable='talker',
            name='minimal_publisher',
            output='screen'  
        ),
        Node(
            package='18225045_Shopee',
            executable='listener',
            name='minimal_subscriber',
            output='screen'  
        )
    ])