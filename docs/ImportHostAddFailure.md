# ImportHostAddFailure

Thrown if failure occurs while adding host to DVS during import operation  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_ip** | **List[str]** | Hosts on which import operation failed  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.import_host_add_failure import ImportHostAddFailure

# TODO update the JSON string below
json = "{}"
# create an instance of ImportHostAddFailure from a JSON string
import_host_add_failure_instance = ImportHostAddFailure.from_json(json)
# print the JSON string representation of the object
print ImportHostAddFailure.to_json()

# convert the object into a dict
import_host_add_failure_dict = import_host_add_failure_instance.to_dict()
# create an instance of ImportHostAddFailure from a dict
import_host_add_failure_form_dict = import_host_add_failure.from_dict(import_host_add_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


