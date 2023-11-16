# DVSMacLearningPolicy

This data object type describes MAC learning policy of a port.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | The flag to indicate if source MAC address learning is allowed.  ***Since:*** vSphere API 6.7  | 
**allow_unicast_flooding** | **bool** | The flag to allow flooding of unlearned MAC for ingress traffic.  ***Since:*** vSphere API 6.7  | [optional] 
**limit** | **int** | The maximum number of MAC addresses that can be learned.  ***Since:*** vSphere API 6.7  | [optional] 
**limit_policy** | **str** | The default switching policy after MAC limit is exceeded.  See *DVSMacLimitPolicyType_enum* for valid values.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.dvs_mac_learning_policy import DVSMacLearningPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of DVSMacLearningPolicy from a JSON string
dvs_mac_learning_policy_instance = DVSMacLearningPolicy.from_json(json)
# print the JSON string representation of the object
print DVSMacLearningPolicy.to_json()

# convert the object into a dict
dvs_mac_learning_policy_dict = dvs_mac_learning_policy_instance.to_dict()
# create an instance of DVSMacLearningPolicy from a dict
dvs_mac_learning_policy_form_dict = dvs_mac_learning_policy.from_dict(dvs_mac_learning_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


