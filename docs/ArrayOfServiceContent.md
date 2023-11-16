# ArrayOfServiceContent

A boxed array of *ServiceContent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ServiceContent]**](ServiceContent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_service_content import ArrayOfServiceContent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfServiceContent from a JSON string
array_of_service_content_instance = ArrayOfServiceContent.from_json(json)
# print the JSON string representation of the object
print ArrayOfServiceContent.to_json()

# convert the object into a dict
array_of_service_content_dict = array_of_service_content_instance.to_dict()
# create an instance of ArrayOfServiceContent from a dict
array_of_service_content_form_dict = array_of_service_content.from_dict(array_of_service_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


