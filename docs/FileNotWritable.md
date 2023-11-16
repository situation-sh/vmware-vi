# FileNotWritable

Thrown if an attempt is made to write to a read-only file. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.file_not_writable import FileNotWritable

# TODO update the JSON string below
json = "{}"
# create an instance of FileNotWritable from a JSON string
file_not_writable_instance = FileNotWritable.from_json(json)
# print the JSON string representation of the object
print FileNotWritable.to_json()

# convert the object into a dict
file_not_writable_dict = file_not_writable_instance.to_dict()
# create an instance of FileNotWritable from a dict
file_not_writable_form_dict = file_not_writable.from_dict(file_not_writable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


