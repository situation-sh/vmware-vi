# ID

This data object type describes an identifier class which is globally unique to identify the associated object.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id string which is globally unique to identify an object.  ***Since:*** vSphere API 6.5  | 

## Example

```python
from vmware_vi.models.id import ID

# TODO update the JSON string below
json = "{}"
# create an instance of ID from a JSON string
id_instance = ID.from_json(json)
# print the JSON string representation of the object
print ID.to_json()

# convert the object into a dict
id_dict = id_instance.to_dict()
# create an instance of ID from a dict
id_form_dict = id.from_dict(id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


