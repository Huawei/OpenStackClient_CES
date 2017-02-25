Command Samples
===============

1. metric list (查询指标列表)::

    $  openstack metric list --namespace=SYS.VPC --metric-name=up_bandwidth
        --start=SYS.VPC.up_bandwidth.bandwidth_id:a6e74b9d-e2c8-4bf8-85a2-cc78a04c6cb4
        --os-cloudeye-endpoint-override=https://ces.eu-de.otc.t-systems.com
    +-----------+--------------+--------------------------------------------------------+--------+
    | Namespace | Metric Name  | Dimension                                              | Unit   |
    +-----------+--------------+--------------------------------------------------------+--------+
    | SYS.VPC   | up_bandwidth | [u'bandwidth_id=775c271a-93f7-4a8c-b8fa-da91a9a0dcd4'] | Byte/s |
    | SYS.VPC   | up_bandwidth | [u'bandwidth_id=74cf708f-9c1e-4f32-bd83-9b945dfe9434'] | Byte/s |
    | SYS.VPC   | up_bandwidth | [u'bandwidth_id=59ab20fd-53c8-44ce-ba03-19dc2f6f038f'] | Byte/s |
    | SYS.VPC   | up_bandwidth | [u'bandwidth_id=38d50758-da39-4d3f-9ee0-9bd78050f682'] | Byte/s |
    | SYS.VPC   | up_bandwidth | [u'bandwidth_id=1d101781-c5ca-47f2-a848-dab03ad341f3'] | Byte/s |
    | SYS.VPC   | up_bandwidth | [u'bandwidth_id=1607470e-8542-40a6-a826-a3e3affff2fc'] | Byte/s |
    | SYS.VPC   | up_bandwidth | [u'bandwidth_id=13b617cd-459c-4351-87a7-ed85e9e59f9d'] | Byte/s |
    | SYS.VPC   | up_bandwidth | [u'bandwidth_id=0c2d5910-55ad-4406-8ee5-fed14a76d0c3'] | Byte/s |
    | SYS.VPC   | up_bandwidth | [u'bandwidth_id=0082ecc5-a7f4-47c2-9196-6fefb4394019'] | Byte/s |
    +-----------+--------------+--------------------------------------------------------+--------+

    $ openstack metric list --dimensions=bandwidth_id=775c271a-93f7-4a8c-b8fa-da91a9a0dcd4
    +-----------+----------------+--------------------------------------------------------+--------+
    | Namespace | Metric Name    | Dimension                                              | Unit   |
    +-----------+----------------+--------------------------------------------------------+--------+
    | SYS.VPC   | up_bandwidth   | [u'bandwidth_id=59ab20fd-53c8-44ce-ba03-19dc2f6f038f'] | Byte/s |
    | SYS.VPC   | down_bandwidth | [u'bandwidth_id=59ab20fd-53c8-44ce-ba03-19dc2f6f038f'] | Byte/s |
    +-----------+----------------+--------------------------------------------------------+--------+

#. metric list (查询已关注指标)::

    $  openstack metric favorite list --os-cloudeye-endpoint-override=https://ces.eu-de.otc.t-systems.com
    +-----------+---------------------------------------+-------------------------------------------------------+
    | Namespace | Metric Name                           | Dimension                                             |
    +-----------+---------------------------------------+-------------------------------------------------------+
    | SYS.AS    | instance_num                          | AutoScalingGroup=56e25174-c317-4be1-9fbd-17d5aff10ad5 |
    | SYS.ECS   | cpu_util                              | instance_id=b9b0ae24-4688-44c6-ae86-19284a774e78      |
    | SYS.ECS   | cpu_util                              | instance_id=3507ae50-95d7-4227-a939-c8f5702dc3f3      |
    | SYS.ECS   | network_outgoing_bytes_aggregate_rate | instance_id=5b4c1602-fb6d-4f1e-87a8-dcf21d9654ba      |
    | SYS.VPC   | down_bandwidth                        | bandwidth_id=1607470e-8542-40a6-a826-a3e3affff2fc     |
    +-----------+---------------------------------------+-------------------------------------------------------+

#. alarm list (查询告警规则列表)::

    $ openstack alarm list --limit=2 --os-cloudeye-endpoint-override=https://ces.eu-de.otc.t-systems.com
    +--------------------------+---------------------+-------------+------------------+---------------------------------------+--------+
    | id                       | name                | desc        | metric namespace | metric name                           | status |
    +--------------------------+---------------------+-------------+------------------+---------------------------------------+--------+
    | al1483387711418ZNpR8DX3g | ECS-Alarm-maas-filp |             | SYS.ECS          | network_incoming_bytes_aggregate_rate | ok     |
    | al1480513400538j1dVGjE04 | as-alarm-5wrm       | autoScaling | SYS.AS           | cpu_util                              | ok     |
    +--------------------------+---------------------+-------------+------------------+---------------------------------------+--------+


#. alarm show (查询单条告警规则信息)::

    $  openstack alarm show al1483387711418ZNpR8DX3g
    +-------------------+--------------------------------------------------+
    | Field             | Value                                            |
    +-------------------+--------------------------------------------------+
    | id                | al1483387711418ZNpR8DX3g                         |
    | name              | ECS-Alarm-maas-filp                              |
    | desc              |                                                  |
    | metric namespace  | SYS.ECS                                          |
    | metric name       | network_incoming_bytes_aggregate_rate            |
    | metric dimensions | instance_id=5b4c1602-fb6d-4f1e-87a8-dcf21d9654ba |
    | condition         | Event average>=100 occurs 3 times in 300 seconds |
    | enabled           | True                                             |
    | action enabled    | False                                            |
    | update time       | 2017-01-19 10:11:55                              |
    | status            | ok                                               |
    +-------------------+--------------------------------------------------+


#. alarm enable (启用告警规则)::

    $  openstack alarm enable al1483387711418ZNpR8DX3g
    Alarm al1483387711418ZNpR8DX3g has been enabled


#. alarm disable (停用告警规则)::

    $  openstack alarm disable al1483387711418ZNpR8DX3g
    Alarm al1483387711418ZNpR8DX3g has been disabled


#. metric data list (查询监控数据)::

    $ openstack metric data list --namespace=SYS.ECS --metric-name=cpu_util --filter=max
     --period=1 --from=1485698044212 --to=1485699044212 --dimension=instance_id=14271c29-143d-4383-b44c-7013fd840be0
    +---------------+-----+------+
    | timestamp     | max | unit |
    +---------------+-----+------+
    | 1485698160000 |   0 | %    |
    | 1485698400000 |   0 | %    |
    | 1485698640000 |   0 | %    |
    | 1485698880000 |   0 | %    |
    +---------------+-----+------+

#. metric data create (添加监控数据)::

    $ openstack metric data create --namespace=woo.ecs --metric-name=cpu_util --dimension=instance_id=14271c29-143d-4383-b44c-7013fd840be0 --ttl 604800 --collect-time=1485699044212 --value=10 --unit=% --type=int --debug
    Metric data has been added

#. quota list (查询配额)::

    $ openstack quota list
    +-------+-------+------+------+
    | type  | quota | used | unit |
    +-------+-------+------+------+
    | alarm |   100 |    4 |      |
    +-------+-------+------+------+


