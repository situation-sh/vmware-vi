# DVSUplinkPortPolicy

The base class for uplink port policy.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.dvs_uplink_port_policy import DVSUplinkPortPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of DVSUplinkPortPolicy from a JSON string
dvs_uplink_port_policy_instance = DVSUplinkPortPolicy.from_json(json)
# print the JSON string representation of the object
print DVSUplinkPortPolicy.to_json()

# convert the object into a dict
dvs_uplink_port_policy_dict = dvs_uplink_port_policy_instance.to_dict()
# create an instance of DVSUplinkPortPolicy from a dict
dvs_uplink_port_policy_form_dict = dvs_uplink_port_policy.from_dict(dvs_uplink_port_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


