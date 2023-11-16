# MultiWriterNotSupported

The multi-writer sharing of the specified virtual disk is not supported.  Typically, this fault is returned as part of a parent fault like *VmConfigIncompatibleForFaultTolerance*, indicating that the virtual disk's multi-writer sharing needs to be changed before fault tolerance can be enabled on the associated virtual machine.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.multi_writer_not_supported import MultiWriterNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of MultiWriterNotSupported from a JSON string
multi_writer_not_supported_instance = MultiWriterNotSupported.from_json(json)
# print the JSON string representation of the object
print MultiWriterNotSupported.to_json()

# convert the object into a dict
multi_writer_not_supported_dict = multi_writer_not_supported_instance.to_dict()
# create an instance of MultiWriterNotSupported from a dict
multi_writer_not_supported_form_dict = multi_writer_not_supported.from_dict(multi_writer_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


