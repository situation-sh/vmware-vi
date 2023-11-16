# ArrayOfServiceLocator

A boxed array of *ServiceLocator*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ServiceLocator]**](ServiceLocator.md) |  | 

## Example

```python
from vmware_vi.models.array_of_service_locator import ArrayOfServiceLocator

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfServiceLocator from a JSON string
array_of_service_locator_instance = ArrayOfServiceLocator.from_json(json)
# print the JSON string representation of the object
print ArrayOfServiceLocator.to_json()

# convert the object into a dict
array_of_service_locator_dict = array_of_service_locator_instance.to_dict()
# create an instance of ArrayOfServiceLocator from a dict
array_of_service_locator_form_dict = array_of_service_locator.from_dict(array_of_service_locator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


