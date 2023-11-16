# UpdateHppMultipathLunPolicyRequestType

The parameters of *HostStorageSystem.UpdateHppMultipathLunPolicy*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lun_id** | **str** | The logical unit ID  | 
**policy** | [**HostMultipathInfoHppLogicalUnitPolicy**](HostMultipathInfoHppLogicalUnitPolicy.md) |  | 

## Example

```python
from vmware_vi.models.update_hpp_multipath_lun_policy_request_type import UpdateHppMultipathLunPolicyRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHppMultipathLunPolicyRequestType from a JSON string
update_hpp_multipath_lun_policy_request_type_instance = UpdateHppMultipathLunPolicyRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateHppMultipathLunPolicyRequestType.to_json()

# convert the object into a dict
update_hpp_multipath_lun_policy_request_type_dict = update_hpp_multipath_lun_policy_request_type_instance.to_dict()
# create an instance of UpdateHppMultipathLunPolicyRequestType from a dict
update_hpp_multipath_lun_policy_request_type_form_dict = update_hpp_multipath_lun_policy_request_type.from_dict(update_hpp_multipath_lun_policy_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


