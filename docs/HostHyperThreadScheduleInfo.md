# HostHyperThreadScheduleInfo

This data object type describes the CpuSchedulerSystem configuration for optimizing hyperthreading.  The primary hyperthreading optimization employed by the CpuSchedulerSystem is to utilize hyperthreads as additional schedulable resources. Although hyperthreads provide limited additional concurrency, certain workloads (such as idling) can take advantage of these hyperthreads. This is particularly useful for SMP virtual machines that use gang scheduling. (Gang scheduling refers to a situation in which all of a parallel program's tasks are grouped into a \"gang\" and concurrently scheduled on distinct processors of a parallel computer system.)  Changes to the hyperthreading optimization can take effect only after a system restart. Therefore, while it is possible to change the configuration at any time, the change will take effect only on the next boot. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | The flag to indicate whether or not hyperthreading optimization is available on the system.  This property is set by VMware prior to installation.  | 
**active** | **bool** | The flag to indicate whether or not the CPU scheduler is currently treating hyperthreads as schedulable resources.  Setting this property involves a successful invocation of either the *enableHyperThreading()* method (\&quot;true\&quot;) or the *disableHyperthreading()* method (\&quot;false\&quot;). The property is set once the system is rebooted.  | 
**config** | **bool** | The flag to indicate whether or not the CPU scheduler should treat hyperthreads as schedulable resources the next time the CPU scheduler starts. - This property is set to \&quot;true\&quot; by successfully invoking the   *enableHyperThreading()* method. - This property is set to \&quot;false\&quot; by successfully invoking the   *disableHyperthreading()* method.  | 

## Example

```python
from vmware_vi.models.host_hyper_thread_schedule_info import HostHyperThreadScheduleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostHyperThreadScheduleInfo from a JSON string
host_hyper_thread_schedule_info_instance = HostHyperThreadScheduleInfo.from_json(json)
# print the JSON string representation of the object
print HostHyperThreadScheduleInfo.to_json()

# convert the object into a dict
host_hyper_thread_schedule_info_dict = host_hyper_thread_schedule_info_instance.to_dict()
# create an instance of HostHyperThreadScheduleInfo from a dict
host_hyper_thread_schedule_info_form_dict = host_hyper_thread_schedule_info.from_dict(host_hyper_thread_schedule_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


