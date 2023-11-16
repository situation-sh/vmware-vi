# RescanHbaRequestType

The parameters of *HostStorageSystem.RescanHba*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hba_device** | **str** | The device of the host bus adapter.  | 

## Example

```python
from vmware_vi.models.rescan_hba_request_type import RescanHbaRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RescanHbaRequestType from a JSON string
rescan_hba_request_type_instance = RescanHbaRequestType.from_json(json)
# print the JSON string representation of the object
print RescanHbaRequestType.to_json()

# convert the object into a dict
rescan_hba_request_type_dict = rescan_hba_request_type_instance.to_dict()
# create an instance of RescanHbaRequestType from a dict
rescan_hba_request_type_form_dict = rescan_hba_request_type.from_dict(rescan_hba_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


