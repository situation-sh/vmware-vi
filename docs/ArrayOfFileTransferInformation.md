# ArrayOfFileTransferInformation

A boxed array of *FileTransferInformation*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FileTransferInformation]**](FileTransferInformation.md) |  | 

## Example

```python
from vmware_vi.models.array_of_file_transfer_information import ArrayOfFileTransferInformation

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFileTransferInformation from a JSON string
array_of_file_transfer_information_instance = ArrayOfFileTransferInformation.from_json(json)
# print the JSON string representation of the object
print ArrayOfFileTransferInformation.to_json()

# convert the object into a dict
array_of_file_transfer_information_dict = array_of_file_transfer_information_instance.to_dict()
# create an instance of ArrayOfFileTransferInformation from a dict
array_of_file_transfer_information_form_dict = array_of_file_transfer_information.from_dict(array_of_file_transfer_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


