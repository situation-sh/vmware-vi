# HostAssignableHardwareBinding

Data object indicating a device instance has been allocated to a VM.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **str** | Instance ID of assigned device.  ***Since:*** vSphere API 7.0  | 
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.host_assignable_hardware_binding import HostAssignableHardwareBinding

# TODO update the JSON string below
json = "{}"
# create an instance of HostAssignableHardwareBinding from a JSON string
host_assignable_hardware_binding_instance = HostAssignableHardwareBinding.from_json(json)
# print the JSON string representation of the object
print HostAssignableHardwareBinding.to_json()

# convert the object into a dict
host_assignable_hardware_binding_dict = host_assignable_hardware_binding_instance.to_dict()
# create an instance of HostAssignableHardwareBinding from a dict
host_assignable_hardware_binding_form_dict = host_assignable_hardware_binding.from_dict(host_assignable_hardware_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


