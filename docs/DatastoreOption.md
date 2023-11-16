# DatastoreOption

The DatastoreOption data object describes datastore options for a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unsupported_volumes** | [**List[VirtualMachineDatastoreVolumeOption]**](VirtualMachineDatastoreVolumeOption.md) | The type of file system volumes on which this virtual machine cannot have its disk and configuration files.  | [optional] 

## Example

```python
from vmware_vi.models.datastore_option import DatastoreOption

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreOption from a JSON string
datastore_option_instance = DatastoreOption.from_json(json)
# print the JSON string representation of the object
print DatastoreOption.to_json()

# convert the object into a dict
datastore_option_dict = datastore_option_instance.to_dict()
# create an instance of DatastoreOption from a dict
datastore_option_form_dict = datastore_option.from_dict(datastore_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


