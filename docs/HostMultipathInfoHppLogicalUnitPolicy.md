# HostMultipathInfoHppLogicalUnitPolicy

The *HostMultipathInfoHppLogicalUnitPolicy* data object describes a multipathing policy for a HPP claimed logical unit and its configuration.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes** | **int** | Byte count on the paths will be used as criteria to switch path for the device.  Allowed values 1 to (100\\*1024\\*1024) Default Value 10\\*1024\\*1024  ***Since:*** vSphere API 7.0  | [optional] 
**iops** | **int** | IOPS count on the paths will be used as criteria to switch path for the device.  Allowed values 1 to 10000 Default Value 1000  ***Since:*** vSphere API 7.0  | [optional] 
**path** | **str** | The preferred path for the given device.  If no prefered path is specified by the user, algorithem at ESX side will choose the random possible path.  ***Since:*** vSphere API 7.0  | [optional] 
**latency_eval_time** | **int** | This value can control at what interval (in ms) the latency of paths should be evaluated.  Allowed values 10000 to (300 \\* 1000) in ms Default Value 30 \\* 1000  ***Since:*** vSphere API 7.0  | [optional] 
**sampling_ios_per_path** | **int** | This value will control how many sample IOs should be issued on each path to calculate latency of the path.  Allowed values 16 to 160 Default Value 16  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.host_multipath_info_hpp_logical_unit_policy import HostMultipathInfoHppLogicalUnitPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of HostMultipathInfoHppLogicalUnitPolicy from a JSON string
host_multipath_info_hpp_logical_unit_policy_instance = HostMultipathInfoHppLogicalUnitPolicy.from_json(json)
# print the JSON string representation of the object
print HostMultipathInfoHppLogicalUnitPolicy.to_json()

# convert the object into a dict
host_multipath_info_hpp_logical_unit_policy_dict = host_multipath_info_hpp_logical_unit_policy_instance.to_dict()
# create an instance of HostMultipathInfoHppLogicalUnitPolicy from a dict
host_multipath_info_hpp_logical_unit_policy_form_dict = host_multipath_info_hpp_logical_unit_policy.from_dict(host_multipath_info_hpp_logical_unit_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


