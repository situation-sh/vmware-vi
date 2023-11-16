# VirtualMachineCertThumbprint

Describes a single certificate thumbprint that can be used to verify the identity of the host before connecting to a running virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thumbprint** | **str** | The thumbprint of the certificate of the host to which we are connecting.  | 
**hash_algorithm** | **str** | The hash algorithm used to generate the thumbprint.  *VirtualMachineCertThumbprintHashAlgorithm_enum* lists the set of supported values.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_cert_thumbprint import VirtualMachineCertThumbprint

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineCertThumbprint from a JSON string
virtual_machine_cert_thumbprint_instance = VirtualMachineCertThumbprint.from_json(json)
# print the JSON string representation of the object
print VirtualMachineCertThumbprint.to_json()

# convert the object into a dict
virtual_machine_cert_thumbprint_dict = virtual_machine_cert_thumbprint_instance.to_dict()
# create an instance of VirtualMachineCertThumbprint from a dict
virtual_machine_cert_thumbprint_form_dict = virtual_machine_cert_thumbprint.from_dict(virtual_machine_cert_thumbprint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


