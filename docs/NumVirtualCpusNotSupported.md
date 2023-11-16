# NumVirtualCpusNotSupported

The host's software does not support enough virtual CPUs to accommodate the virtual machine.  This is always an error. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_supported_vcpus_dest** | **int** | The maximum number of virtual CPUs supported on the host.  | 
**num_cpu_vm** | **int** | The number of virtual CPUs in the virtual machine.  | 

## Example

```python
from vmware_vi.models.num_virtual_cpus_not_supported import NumVirtualCpusNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of NumVirtualCpusNotSupported from a JSON string
num_virtual_cpus_not_supported_instance = NumVirtualCpusNotSupported.from_json(json)
# print the JSON string representation of the object
print NumVirtualCpusNotSupported.to_json()

# convert the object into a dict
num_virtual_cpus_not_supported_dict = num_virtual_cpus_not_supported_instance.to_dict()
# create an instance of NumVirtualCpusNotSupported from a dict
num_virtual_cpus_not_supported_form_dict = num_virtual_cpus_not_supported.from_dict(num_virtual_cpus_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


