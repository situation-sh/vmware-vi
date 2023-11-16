# DVSContactInfo

Contact information of a human operator.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the person who is responsible for the switch.  ***Since:*** vSphere API 4.0  | [optional] 
**contact** | **str** | The contact information for the person.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.dvs_contact_info import DVSContactInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DVSContactInfo from a JSON string
dvs_contact_info_instance = DVSContactInfo.from_json(json)
# print the JSON string representation of the object
print DVSContactInfo.to_json()

# convert the object into a dict
dvs_contact_info_dict = dvs_contact_info_instance.to_dict()
# create an instance of DVSContactInfo from a dict
dvs_contact_info_form_dict = dvs_contact_info.from_dict(dvs_contact_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


