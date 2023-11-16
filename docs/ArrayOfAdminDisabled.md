# ArrayOfAdminDisabled

A boxed array of *AdminDisabled*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AdminDisabled]**](AdminDisabled.md) |  | 

## Example

```python
from vmware_vi.models.array_of_admin_disabled import ArrayOfAdminDisabled

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAdminDisabled from a JSON string
array_of_admin_disabled_instance = ArrayOfAdminDisabled.from_json(json)
# print the JSON string representation of the object
print ArrayOfAdminDisabled.to_json()

# convert the object into a dict
array_of_admin_disabled_dict = array_of_admin_disabled_instance.to_dict()
# create an instance of ArrayOfAdminDisabled from a dict
array_of_admin_disabled_form_dict = array_of_admin_disabled.from_dict(array_of_admin_disabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


