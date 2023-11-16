# OvfSystemFault

A common base class to host all the OVF subsystems's system faults.  This is a class of fault that can be thrown because of some api changes, new hardware that are not supported by the host.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.ovf_system_fault import OvfSystemFault

# TODO update the JSON string below
json = "{}"
# create an instance of OvfSystemFault from a JSON string
ovf_system_fault_instance = OvfSystemFault.from_json(json)
# print the JSON string representation of the object
print OvfSystemFault.to_json()

# convert the object into a dict
ovf_system_fault_dict = ovf_system_fault_instance.to_dict()
# create an instance of OvfSystemFault from a dict
ovf_system_fault_form_dict = ovf_system_fault.from_dict(ovf_system_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


