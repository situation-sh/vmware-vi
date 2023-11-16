# DVSSecurityPolicy

This data object type describes security policy governing ports.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_promiscuous** | [**BoolPolicy**](BoolPolicy.md) |  | [optional] 
**mac_changes** | [**BoolPolicy**](BoolPolicy.md) |  | [optional] 
**forged_transmits** | [**BoolPolicy**](BoolPolicy.md) |  | [optional] 

## Example

```python
from vmware_vi.models.dvs_security_policy import DVSSecurityPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of DVSSecurityPolicy from a JSON string
dvs_security_policy_instance = DVSSecurityPolicy.from_json(json)
# print the JSON string representation of the object
print DVSSecurityPolicy.to_json()

# convert the object into a dict
dvs_security_policy_dict = dvs_security_policy_instance.to_dict()
# create an instance of DVSSecurityPolicy from a dict
dvs_security_policy_form_dict = dvs_security_policy.from_dict(dvs_security_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


