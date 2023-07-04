package com.example.gateway;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpMethod;
import org.springframework.web.cors.CorsConfiguration;
import org.springframework.web.cors.reactive.CorsWebFilter;
import org.springframework.web.cors.reactive.DefaultCorsProcessor;
import org.springframework.web.cors.reactive.UrlBasedCorsConfigurationSource;
import org.springframework.web.server.ServerWebExchange;
import org.springframework.web.util.pattern.PathPatternParser;

import com.example.gateway.CorsResponseHeaderFilter;
//import com.einwin.platform.sso.common.RequestHeaderKeys;

/**
 * 网关跨域配置
 * @Author 
 * @Create 2019-04-19 15:29:54
 */
@Configuration
public class myCorsConfiguration {
	@Bean
	public CorsResponseHeaderFilter corsResponseHeaderFilter() {
		return new CorsResponseHeaderFilter();
	}
	
	@Bean
	public CorsWebFilter corsFilter() {
		UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource(new PathPatternParser());
		source.registerCorsConfiguration("/**", buildCorsConfiguration());
		
		CorsWebFilter corsWebFilter = new CorsWebFilter(source, new DefaultCorsProcessor() {
			@Override
			protected boolean handleInternal(ServerWebExchange exchange, CorsConfiguration config, 
				boolean preFlightRequest) 
			{
				// 预留扩展点
				// if (exchange.getRequest().getMethod() == HttpMethod.OPTIONS) {
					return super.handleInternal(exchange, config, preFlightRequest);
				// }

				// return true;
			}
		});
		
		return corsWebFilter;
	}
	
	private CorsConfiguration buildCorsConfiguration() {
		CorsConfiguration corsConfiguration = new CorsConfiguration();
		corsConfiguration.addAllowedOrigin("http://localhost:8081/");
		corsConfiguration.addAllowedOrigin("http://localhost:8082/");

		corsConfiguration.addAllowedMethod(HttpMethod.OPTIONS);
		corsConfiguration.addAllowedMethod(HttpMethod.POST);
		corsConfiguration.addAllowedMethod(HttpMethod.GET);
		corsConfiguration.addAllowedMethod(HttpMethod.PUT);
		corsConfiguration.addAllowedMethod(HttpMethod.DELETE);
		corsConfiguration.addAllowedMethod(HttpMethod.PATCH);
		// corsConfiguration.addAllowedMethod("*");
		
		corsConfiguration.addAllowedHeader("origin");
		corsConfiguration.addAllowedHeader("content-type");
		corsConfiguration.addAllowedHeader("accept");
		corsConfiguration.addAllowedHeader("x-requested-with");
		corsConfiguration.addAllowedHeader("Referer");
//		corsConfiguration.addAllowedHeader(RequestHeaderKeys.USER_AGENT);
//		corsConfiguration.addAllowedHeader(RequestHeaderKeys.TOKEN);
//		corsConfiguration.addAllowedHeader(RequestHeaderKeys.REFRESH_TOKEN);
//		corsConfiguration.addAllowedHeader(RequestHeaderKeys.OS);
//		corsConfiguration.addAllowedHeader(RequestHeaderKeys.X_APP_KEY);
//		corsConfiguration.addAllowedHeader(RequestHeaderKeys.X_DEVICE_ID);
//		corsConfiguration.addAllowedHeader(RequestHeaderKeys.X_TOKEN);
		// corsConfiguration.addAllowedHeader("*");
		
		corsConfiguration.setMaxAge(7200L);
		corsConfiguration.setAllowCredentials(true);
		return corsConfiguration;
	}
}

