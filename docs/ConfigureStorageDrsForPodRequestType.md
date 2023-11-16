# ConfigureStorageDrsForPodRequestType

The parameters of *StorageResourceManager.ConfigureStorageDrsForPod_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pod** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**spec** | [**StorageDrsConfigSpec**](StorageDrsConfigSpec.md) |  | 
**modify** | **bool** | Flag to specify whether the specification (\&quot;spec\&quot;) should be applied incrementally. If \&quot;modify\&quot; is false and the operation succeeds, then the configuration of the storage pod matches the specification exactly; in this case any unset portions of the specification will result in unset or default portions of the configuration.  | 

## Example

```python
from vmware_vi.models.configure_storage_drs_for_pod_request_type import ConfigureStorageDrsForPodRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigureStorageDrsForPodRequestType from a JSON string
configure_storage_drs_for_pod_request_type_instance = ConfigureStorageDrsForPodRequestType.from_json(json)
# print the JSON string representation of the object
print ConfigureStorageDrsForPodRequestType.to_json()

# convert the object into a dict
configure_storage_drs_for_pod_request_type_dict = configure_storage_drs_for_pod_request_type_instance.to_dict()
# create an instance of ConfigureStorageDrsForPodRequestType from a dict
configure_storage_drs_for_pod_request_type_form_dict = configure_storage_drs_for_pod_request_type.from_dict(configure_storage_drs_for_pod_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


