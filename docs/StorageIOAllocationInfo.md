# StorageIOAllocationInfo

The IOAllocationInfo specifies the shares, limit and reservation for storage I/O resource.  The storage I/O resource is allocated to virtual machines based on their shares, limit and reservation. The reservation is currently exposed only at the host level for local and shared datastores. We do not support storage I/O resource management on resource pools.  Each virtual machine has one IOAllocationInfo object per virtual disk. For example, we can specify that a virtual machine has 500 shares on the first virtual disk, 1000 shares on the second virtual disk, etc.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The utilization of a virtual machine will not exceed this limit, even if there are available resources.  This is typically used to ensure a consistent performance of virtual machines independent of available resources. If set to -1, then there is no fixed limit on resource usage (only bounded by available resources and shares). The unit is number of I/O per second. While setting the limit for storage I/O resource, if the property is unset, it is treated as no change and the property is not updated. While reading back the limit information of storage I/O resource, if the property is unset, a default value of -1 will be returned, which indicates that there is no limit on resource usage.  ***Since:*** vSphere API 4.1  | [optional] 
**shares** | [**SharesInfo**](SharesInfo.md) |  | [optional] 
**reservation** | **int** | Reservation control is used to provide guaranteed allocation in terms of IOPS.  Large IO sizes are considered as multiple IOs using a chunk size of 32 KB as default. This control is initially supported only at host level for local datastores. It future, it may get supported on shared storage based on integration with Storage IO Control. Also right now we don&#39;t do any admission control based on IO reservation values.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.storage_io_allocation_info import StorageIOAllocationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StorageIOAllocationInfo from a JSON string
storage_io_allocation_info_instance = StorageIOAllocationInfo.from_json(json)
# print the JSON string representation of the object
print StorageIOAllocationInfo.to_json()

# convert the object into a dict
storage_io_allocation_info_dict = storage_io_allocation_info_instance.to_dict()
# create an instance of StorageIOAllocationInfo from a dict
storage_io_allocation_info_form_dict = storage_io_allocation_info.from_dict(storage_io_allocation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


