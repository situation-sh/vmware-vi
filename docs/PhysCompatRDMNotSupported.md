# PhysCompatRDMNotSupported

The virtual machine is configured with a Raw Disk Mapping in physical compatibility mode.  This mode is not supported on the host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.phys_compat_rdm_not_supported import PhysCompatRDMNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of PhysCompatRDMNotSupported from a JSON string
phys_compat_rdm_not_supported_instance = PhysCompatRDMNotSupported.from_json(json)
# print the JSON string representation of the object
print PhysCompatRDMNotSupported.to_json()

# convert the object into a dict
phys_compat_rdm_not_supported_dict = phys_compat_rdm_not_supported_instance.to_dict()
# create an instance of PhysCompatRDMNotSupported from a dict
phys_compat_rdm_not_supported_form_dict = phys_compat_rdm_not_supported.from_dict(phys_compat_rdm_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


