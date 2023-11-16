# NumVirtualCpusIncompatible

The number of virtual CPUs present or requested in the virtual machine's configuration is not supported for a specific feature.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The reason for the incompatibility.  See *NumVirtualCpusIncompatibleReason_enum* for valid values.  ***Since:*** vSphere API 4.0  | 
**num_cpu** | **int** | The number of virtual CPUs in the virtual machine.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.num_virtual_cpus_incompatible import NumVirtualCpusIncompatible

# TODO update the JSON string below
json = "{}"
# create an instance of NumVirtualCpusIncompatible from a JSON string
num_virtual_cpus_incompatible_instance = NumVirtualCpusIncompatible.from_json(json)
# print the JSON string representation of the object
print NumVirtualCpusIncompatible.to_json()

# convert the object into a dict
num_virtual_cpus_incompatible_dict = num_virtual_cpus_incompatible_instance.to_dict()
# create an instance of NumVirtualCpusIncompatible from a dict
num_virtual_cpus_incompatible_form_dict = num_virtual_cpus_incompatible.from_dict(num_virtual_cpus_incompatible_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


