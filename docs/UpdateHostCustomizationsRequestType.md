# UpdateHostCustomizationsRequestType

The parameters of *HostProfileManager.UpdateHostCustomizations_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_to_config_spec_map** | [**List[HostProfileManagerHostToConfigSpecMap]**](HostProfileManagerHostToConfigSpecMap.md) | A map that contains the hosts with which the answer files are associated and the corresponding host-specific configuration data. If the configuration specification does not contain any host-specific user input (&lt;code&gt;configSpec&lt;/code&gt;.*AnswerFileOptionsCreateSpec.userInput*), the method does not perform any operation on the answer file.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.update_host_customizations_request_type import UpdateHostCustomizationsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHostCustomizationsRequestType from a JSON string
update_host_customizations_request_type_instance = UpdateHostCustomizationsRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateHostCustomizationsRequestType.to_json()

# convert the object into a dict
update_host_customizations_request_type_dict = update_host_customizations_request_type_instance.to_dict()
# create an instance of UpdateHostCustomizationsRequestType from a dict
update_host_customizations_request_type_form_dict = update_host_customizations_request_type.from_dict(update_host_customizations_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


