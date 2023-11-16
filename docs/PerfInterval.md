# PerfInterval

This data object type contains metadata about a performance interval. - For VirtualCenter Server systems, instances of this data object are   referred to as &#147;historical intervals&#148; because they control   how data collected from the ESX systems will be aggregated and stored   in the database. - For ESX system, this data object is typically referred to simply as the   &#147;interval&#148; or &#147;performance interval&#148; because ESX   does not aggregate statistical data.     For ESX systems, a single instance of this data object exists. It cannot be modified. It has these properties: <table border=\"1\"width=\"100%\"> <tr> <th>key</th> <th>samplingPeriod</th> <th>length</th> <th>name</th> <th>level</th> <th>enabled</th> </tr> <tr> <td>1</td> <td>300</td> <td>129600</td> <td>PastDay</td> <td>null</td> <td>true</td> </tr> </table>  VirtualCenter Server system provides four instances of this data object by default, that apply globally to all system entities.  **Example Collection Levels**   VirtualCenter Server uses the specifications configured in its historical intervals to collect metrics from the ESX systems that it manages. The quantity of data collected depends on the level settings for the server, and the level associated with a specific counter. Both factors may change from one version of the products to the next. In general, the lower the number, the smaller the amount of data collected. For VirtualCenter Server 2.5, for example, the levels 1 through 4 collected data as follows: 1. Basic counters defined with \"average\" *rollup type* for CPU, Memory,    Disk, and Network; plus counters for System Uptime, System Heartbeat,    and DRS (Distributed Resource Scheduler, tracked in the    \"clusterServices\" group). Does not include counters for devices. 2. Counters defined with \"average,\" \"summation,\" and \"latest\" *rollup types* for CPU,    Memory, Disk, and Network; plus counters for System Uptime, System    Heartbeat, and DRS (clusterServices). Does not include counters for    devices. 3. Counters defined with \"average,\" \"summmation,\" and \"latest\" *rollup types* for CPU,    Memory, Disk, Network, and all devices; plus counters for System    Uptime, System Heartbeat, and DRS (clusterServices). 4. All counters defined for all entities and devices, for every *rollup type*, including    &#147;minimum&#148; and &#147;maximum&#46;&#148;      Default properties for the four built-in historical intervals include: <table border=\"1\"width=\"100%\"> <tr> <th>key</th> <th>samplingPeriod</th> <th>length</th> <th>name</th> <th>level</th> <th>enabled</th> </tr> <tr> <td>1</td> <td>300</td> <td>86400</td> <td>Past&nbsp;day</td> <td>1</td> <td>true</td> </tr> <tr> <td>2</td> <td>1800</td> <td>604800</td> <td>Past&nbsp;week</td> <td>1</td> <td>true</td> </tr> <tr> <td>3</td> <td>7200</td> <td>2592000</td> <td>Past&nbsp;month</td> <td>1</td> <td>true</td> </tr> <tr> <td>4</td> <td>86400</td> <td>31536000</td> <td>Past&nbsp;year</td> <td>1</td> <td>true</td> </tr> </table>  All values are in seconds. The default setting for vCenter Server is level 1, which retains sampled statistical data as follows: - 5-minute samples for the past day - 30-minute samples for the past week - 2-hour samples for the past month - 1-day samples for the past year     Data older than a year is purged from the vCenter Server database.  Prior to version 2&#46;5 of the API, this data object could be used in conjunction with the *PerformanceManager.CreatePerfInterval* operation, to define new, custom historical intervals. That operation has been deprecated: Adding and deleting objects of this type is no longer supported. However, the default historical intervals can be enabled or disabled, and can be modified within certain limits (with the *PerformanceManager.UpdatePerfInterval* operation)&#46; 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **int** | A unique identifier for the interval.  ***Since:*** VI API 2.5  | 
**sampling_period** | **int** | Number of seconds that data is sampled for this interval.  The real-time samplingPeriod is 20 seconds.  | 
**name** | **str** | The name of the historical interval.  A localized string that provides a name for the interval. Names include: - \&quot;Past Day\&quot; - \&quot;Past Week\&quot; - \&quot;Past Month\&quot; - \&quot;Past Year\&quot;    The name is not meaningful in terms of system behavior. That is, the interval named &amp;#147;Past Week&amp;#148; works as it does because of its length, level, and so on, not because of the value of this string.  | 
**length** | **int** | Number of seconds that the statistics corresponding to this interval are kept on the system.  | 
**level** | **int** | Statistics collection level for this historical interval.  vCenter Server will aggregate only those statistics that match the value of this property for this historical interval. For ESX, the value of this property is null. For vCenter Server, the value will be a number from 1 to 4.  ***Since:*** VI API 2.5  | [optional] 
**enabled** | **bool** | Indicates whether the interval is enabled (true) or disabled (false).  Disabling a historical interval prevents vCenter Server from collecting metrics for that interval and all higher (longer) intervals.  For example, disabling the \&quot;Past Month\&quot; interval disables both \&quot;Past Month\&quot; and \&quot;Past Year\&quot; intervals. The system will aggregate and retain performance data using the \&quot;Past Day\&quot; and \&quot;Past Week\&quot; intervals only.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.perf_interval import PerfInterval

# TODO update the JSON string below
json = "{}"
# create an instance of PerfInterval from a JSON string
perf_interval_instance = PerfInterval.from_json(json)
# print the JSON string representation of the object
print PerfInterval.to_json()

# convert the object into a dict
perf_interval_dict = perf_interval_instance.to_dict()
# create an instance of PerfInterval from a dict
perf_interval_form_dict = perf_interval.from_dict(perf_interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


