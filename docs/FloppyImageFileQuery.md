# FloppyImageFileQuery

This data object type describes the query specification for a floppy disk image. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.floppy_image_file_query import FloppyImageFileQuery

# TODO update the JSON string below
json = "{}"
# create an instance of FloppyImageFileQuery from a JSON string
floppy_image_file_query_instance = FloppyImageFileQuery.from_json(json)
# print the JSON string representation of the object
print FloppyImageFileQuery.to_json()

# convert the object into a dict
floppy_image_file_query_dict = floppy_image_file_query_instance.to_dict()
# create an instance of FloppyImageFileQuery from a dict
floppy_image_file_query_form_dict = floppy_image_file_query.from_dict(floppy_image_file_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


