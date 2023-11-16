# ArrayOfNotAuthenticated

A boxed array of *NotAuthenticated*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NotAuthenticated]**](NotAuthenticated.md) |  | 

## Example

```python
from vmware_vi.models.array_of_not_authenticated import ArrayOfNotAuthenticated

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNotAuthenticated from a JSON string
array_of_not_authenticated_instance = ArrayOfNotAuthenticated.from_json(json)
# print the JSON string representation of the object
print ArrayOfNotAuthenticated.to_json()

# convert the object into a dict
array_of_not_authenticated_dict = array_of_not_authenticated_instance.to_dict()
# create an instance of ArrayOfNotAuthenticated from a dict
array_of_not_authenticated_form_dict = array_of_not_authenticated.from_dict(array_of_not_authenticated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


