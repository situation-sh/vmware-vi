# GenerateHostConfigTaskSpecRequestType

The parameters of *HostProfileManager.GenerateHostConfigTaskSpec_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts_info** | [**List[StructuredCustomizations]**](StructuredCustomizations.md) | List of host data for which configuration task list needs to be generated. The *StructuredCustomizations.customizations* value should be provided only if the host customization data for that host is invalid. If this property is not provided, the API will use the host customization data stored in VC and generate task list.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.generate_host_config_task_spec_request_type import GenerateHostConfigTaskSpecRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateHostConfigTaskSpecRequestType from a JSON string
generate_host_config_task_spec_request_type_instance = GenerateHostConfigTaskSpecRequestType.from_json(json)
# print the JSON string representation of the object
print GenerateHostConfigTaskSpecRequestType.to_json()

# convert the object into a dict
generate_host_config_task_spec_request_type_dict = generate_host_config_task_spec_request_type_instance.to_dict()
# create an instance of GenerateHostConfigTaskSpecRequestType from a dict
generate_host_config_task_spec_request_type_form_dict = generate_host_config_task_spec_request_type.from_dict(generate_host_config_task_spec_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


