# Description

Static strings used for describing an object or property. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Display label.  | 
**summary** | **str** | Summary description.  | 

## Example

```python
from vmware_vi.models.description import Description

# TODO update the JSON string below
json = "{}"
# create an instance of Description from a JSON string
description_instance = Description.from_json(json)
# print the JSON string representation of the object
print Description.to_json()

# convert the object into a dict
description_dict = description_instance.to_dict()
# create an instance of Description from a dict
description_form_dict = description.from_dict(description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


