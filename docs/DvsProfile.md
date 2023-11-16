# DvsProfile

The *DvsProfile* data object represents the distributed virtual switch to which this host is connected.  If a profile plug-in defines policies or subprofiles, use the *ApplyProfile.policy* or *ApplyProfile.property* list to access the additional configuration data.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Linkable identifier.  ***Since:*** vSphere API 4.0  | 
**name** | **str** | Unique identifier for the distributed virtual switch.  ***Since:*** vSphere API 4.0  | 
**uplink** | [**List[PnicUplinkProfile]**](PnicUplinkProfile.md) | List of subprofiles that map physical NICs to uplink ports.  Use the *PnicUplinkProfile.key* property to access subprofiles in the list.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.dvs_profile import DvsProfile

# TODO update the JSON string below
json = "{}"
# create an instance of DvsProfile from a JSON string
dvs_profile_instance = DvsProfile.from_json(json)
# print the JSON string representation of the object
print DvsProfile.to_json()

# convert the object into a dict
dvs_profile_dict = dvs_profile_instance.to_dict()
# create an instance of DvsProfile from a dict
dvs_profile_form_dict = dvs_profile.from_dict(dvs_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


