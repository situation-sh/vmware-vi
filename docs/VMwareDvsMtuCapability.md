# VMwareDvsMtuCapability

Indicators of support for version-specific supported MTU.  ***Since:*** vSphere API 7.0.2.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_mtu_supported** | **int** | Minimum supported MTU on VDS.  ***Since:*** vSphere API 7.0.2.0  | 
**max_mtu_supported** | **int** | Maximum supported MTU on VDS.  ***Since:*** vSphere API 7.0.2.0  | 

## Example

```python
from vmware_vi.models.v_mware_dvs_mtu_capability import VMwareDvsMtuCapability

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareDvsMtuCapability from a JSON string
v_mware_dvs_mtu_capability_instance = VMwareDvsMtuCapability.from_json(json)
# print the JSON string representation of the object
print VMwareDvsMtuCapability.to_json()

# convert the object into a dict
v_mware_dvs_mtu_capability_dict = v_mware_dvs_mtu_capability_instance.to_dict()
# create an instance of VMwareDvsMtuCapability from a dict
v_mware_dvs_mtu_capability_form_dict = v_mware_dvs_mtu_capability.from_dict(v_mware_dvs_mtu_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


