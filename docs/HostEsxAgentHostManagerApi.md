# vmware_vi.HostEsxAgentHostManagerApi

All URIs are relative to *https://localhost/sdk/vim25/8.0.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_esx_agent_host_manager_esx_agent_host_manager_update_config**](HostEsxAgentHostManagerApi.md#host_esx_agent_host_manager_esx_agent_host_manager_update_config) | **POST** /HostEsxAgentHostManager/{moId}/EsxAgentHostManagerUpdateConfig | Update the host&#39;s ESX agent configuration. 
[**host_esx_agent_host_manager_get_config_info**](HostEsxAgentHostManagerApi.md#host_esx_agent_host_manager_get_config_info) | **GET** /HostEsxAgentHostManager/{moId}/configInfo | Configuration of agent virtual machine resources 


# **host_esx_agent_host_manager_esx_agent_host_manager_update_config**
> host_esx_agent_host_manager_esx_agent_host_manager_update_config(mo_id, esx_agent_host_manager_update_config_request_type)

Update the host's ESX agent configuration. 

Update the host's ESX agent configuration.  The entire configuration must be set each time since all values are overwritten. E.g. a field set to null clears the value on the host.  ***Since:*** vSphere API 5.0  ***Required privileges:*** Host.Config.Settings 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.esx_agent_host_manager_update_config_request_type import EsxAgentHostManagerUpdateConfigRequestType
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostEsxAgentHostManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.
    esx_agent_host_manager_update_config_request_type = vmware_vi.EsxAgentHostManagerUpdateConfigRequestType() # EsxAgentHostManagerUpdateConfigRequestType | 

    try:
        # Update the host's ESX agent configuration. 
        api_instance.host_esx_agent_host_manager_esx_agent_host_manager_update_config(mo_id, esx_agent_host_manager_update_config_request_type)
    except Exception as e:
        print("Exception when calling HostEsxAgentHostManagerApi->host_esx_agent_host_manager_esx_agent_host_manager_update_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 
 **esx_agent_host_manager_update_config_request_type** | [**EsxAgentHostManagerUpdateConfigRequestType**](EsxAgentHostManagerUpdateConfigRequestType.md)|  | 

### Return type

void (empty response body)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content  |  -  |
**500** | ***HostConfigFault***: if an error occurs.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_esx_agent_host_manager_get_config_info**
> HostEsxAgentHostManagerConfigInfo host_esx_agent_host_manager_get_config_info(mo_id)

Configuration of agent virtual machine resources 

Configuration of agent virtual machine resources  ***Since:*** vSphere API 5.0  ***Required privileges:*** Host.Config.Settings 

### Example

* Api Key Authentication (Session):
```python
import time
import os
import vmware_vi
from vmware_vi.models.host_esx_agent_host_manager_config_info import HostEsxAgentHostManagerConfigInfo
from vmware_vi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/sdk/vim25/8.0.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = vmware_vi.Configuration(
    host = "https://localhost/sdk/vim25/8.0.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Session
configuration.api_key['Session'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Enter a context with an instance of the API client
with vmware_vi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vmware_vi.HostEsxAgentHostManagerApi(api_client)
    mo_id = 'mo_id_example' # str | A unique identifier (within this vCenter Server instance) for a specific managed object such as `group-d1` or `vm-015` or `ServiceInstance`.

    try:
        # Configuration of agent virtual machine resources 
        api_response = api_instance.host_esx_agent_host_manager_get_config_info(mo_id)
        print("The response of HostEsxAgentHostManagerApi->host_esx_agent_host_manager_get_config_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostEsxAgentHostManagerApi->host_esx_agent_host_manager_get_config_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mo_id** | **str**| A unique identifier (within this vCenter Server instance) for a specific managed object such as &#x60;group-d1&#x60; or &#x60;vm-015&#x60; or &#x60;ServiceInstance&#x60;. | 

### Return type

[**HostEsxAgentHostManagerConfigInfo**](HostEsxAgentHostManagerConfigInfo.md)

### Authorization

[Session](../README.md#Session)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

