# IsoImageFileQuery

This data object type describes the query specification for an ISO CD-ROM image. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.iso_image_file_query import IsoImageFileQuery

# TODO update the JSON string below
json = "{}"
# create an instance of IsoImageFileQuery from a JSON string
iso_image_file_query_instance = IsoImageFileQuery.from_json(json)
# print the JSON string representation of the object
print IsoImageFileQuery.to_json()

# convert the object into a dict
iso_image_file_query_dict = iso_image_file_query_instance.to_dict()
# create an instance of IsoImageFileQuery from a dict
iso_image_file_query_form_dict = iso_image_file_query.from_dict(iso_image_file_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


