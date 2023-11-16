# ArrayOfVirtualTPM

A boxed array of *VirtualTPM*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualTPM]**](VirtualTPM.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_tpm import ArrayOfVirtualTPM

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualTPM from a JSON string
array_of_virtual_tpm_instance = ArrayOfVirtualTPM.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualTPM.to_json()

# convert the object into a dict
array_of_virtual_tpm_dict = array_of_virtual_tpm_instance.to_dict()
# create an instance of ArrayOfVirtualTPM from a dict
array_of_virtual_tpm_form_dict = array_of_virtual_tpm.from_dict(array_of_virtual_tpm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


