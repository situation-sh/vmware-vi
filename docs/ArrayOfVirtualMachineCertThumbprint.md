# ArrayOfVirtualMachineCertThumbprint

A boxed array of *VirtualMachineCertThumbprint*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineCertThumbprint]**](VirtualMachineCertThumbprint.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_cert_thumbprint import ArrayOfVirtualMachineCertThumbprint

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineCertThumbprint from a JSON string
array_of_virtual_machine_cert_thumbprint_instance = ArrayOfVirtualMachineCertThumbprint.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineCertThumbprint.to_json()

# convert the object into a dict
array_of_virtual_machine_cert_thumbprint_dict = array_of_virtual_machine_cert_thumbprint_instance.to_dict()
# create an instance of ArrayOfVirtualMachineCertThumbprint from a dict
array_of_virtual_machine_cert_thumbprint_form_dict = array_of_virtual_machine_cert_thumbprint.from_dict(array_of_virtual_machine_cert_thumbprint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


