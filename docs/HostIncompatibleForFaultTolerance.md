# HostIncompatibleForFaultTolerance

This fault is thrown when an attempt is made to configure a fault tolerant virtual machine on a host that is incompatible.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** |  | [optional] 
**reason** | **str** | The specific reason why the host does not support fault tolerance.  Values should come from *HostIncompatibleForFaultToleranceReason_enum*.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_incompatible_for_fault_tolerance import HostIncompatibleForFaultTolerance

# TODO update the JSON string below
json = "{}"
# create an instance of HostIncompatibleForFaultTolerance from a JSON string
host_incompatible_for_fault_tolerance_instance = HostIncompatibleForFaultTolerance.from_json(json)
# print the JSON string representation of the object
print HostIncompatibleForFaultTolerance.to_json()

# convert the object into a dict
host_incompatible_for_fault_tolerance_dict = host_incompatible_for_fault_tolerance_instance.to_dict()
# create an instance of HostIncompatibleForFaultTolerance from a dict
host_incompatible_for_fault_tolerance_form_dict = host_incompatible_for_fault_tolerance.from_dict(host_incompatible_for_fault_tolerance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


