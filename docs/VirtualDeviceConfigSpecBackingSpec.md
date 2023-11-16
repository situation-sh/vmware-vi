# VirtualDeviceConfigSpecBackingSpec

<code>*VirtualDeviceConfigSpecBackingSpec*</code> is a data object type for information about configuration of the backing of a device in a virtual machine.  The member *VirtualDeviceConfigSpecBackingSpec.parent* refers the parent in the chain of *VirtualDeviceBackingInfo* objects.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | [**VirtualDeviceConfigSpecBackingSpec**](VirtualDeviceConfigSpecBackingSpec.md) |  | [optional] 
**crypto** | [**CryptoSpec**](CryptoSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_device_config_spec_backing_spec import VirtualDeviceConfigSpecBackingSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDeviceConfigSpecBackingSpec from a JSON string
virtual_device_config_spec_backing_spec_instance = VirtualDeviceConfigSpecBackingSpec.from_json(json)
# print the JSON string representation of the object
print VirtualDeviceConfigSpecBackingSpec.to_json()

# convert the object into a dict
virtual_device_config_spec_backing_spec_dict = virtual_device_config_spec_backing_spec_instance.to_dict()
# create an instance of VirtualDeviceConfigSpecBackingSpec from a dict
virtual_device_config_spec_backing_spec_form_dict = virtual_device_config_spec_backing_spec.from_dict(virtual_device_config_spec_backing_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


