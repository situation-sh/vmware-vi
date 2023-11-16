# ArrayOfHostAccountSpec

A boxed array of *HostAccountSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostAccountSpec]**](HostAccountSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_account_spec import ArrayOfHostAccountSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostAccountSpec from a JSON string
array_of_host_account_spec_instance = ArrayOfHostAccountSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostAccountSpec.to_json()

# convert the object into a dict
array_of_host_account_spec_dict = array_of_host_account_spec_instance.to_dict()
# create an instance of ArrayOfHostAccountSpec from a dict
array_of_host_account_spec_form_dict = array_of_host_account_spec.from_dict(array_of_host_account_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


