# Tag

Defines a tag that can be associated with a managed entity.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The tag key in human readable form.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.tag import Tag

# TODO update the JSON string below
json = "{}"
# create an instance of Tag from a JSON string
tag_instance = Tag.from_json(json)
# print the JSON string representation of the object
print Tag.to_json()

# convert the object into a dict
tag_dict = tag_instance.to_dict()
# create an instance of Tag from a dict
tag_form_dict = tag.from_dict(tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


