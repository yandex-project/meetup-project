(function(e){function t(t){for(var a,i,r=t[0],n=t[1],c=t[2],p=0,m=[];p<r.length;p++)i=r[p],Object.prototype.hasOwnProperty.call(s,i)&&s[i]&&m.push(s[i][0]),s[i]=0;for(a in n)Object.prototype.hasOwnProperty.call(n,a)&&(e[a]=n[a]);d&&d(t);while(m.length)m.shift()();return l.push.apply(l,c||[]),o()}function o(){for(var e,t=0;t<l.length;t++){for(var o=l[t],a=!0,r=1;r<o.length;r++){var n=o[r];0!==s[n]&&(a=!1)}a&&(l.splice(t--,1),e=i(i.s=o[0]))}return e}var a={},s={app:0},l=[];function i(t){if(a[t])return a[t].exports;var o=a[t]={i:t,l:!1,exports:{}};return e[t].call(o.exports,o,o.exports,i),o.l=!0,o.exports}i.m=e,i.c=a,i.d=function(e,t,o){i.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:o})},i.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.t=function(e,t){if(1&t&&(e=i(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var o=Object.create(null);if(i.r(o),Object.defineProperty(o,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var a in e)i.d(o,a,function(t){return e[t]}.bind(null,a));return o},i.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return i.d(t,"a",t),t},i.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},i.p="/";var r=window["webpackJsonp"]=window["webpackJsonp"]||[],n=r.push.bind(r);r.push=t,r=r.slice();for(var c=0;c<r.length;c++)t(r[c]);var d=n;l.push([0,"chunk-vendors"]),o()})({0:function(e,t,o){e.exports=o("56d7")},"2f99":function(e,t,o){"use strict";o("af57")},"56d7":function(e,t,o){"use strict";o.r(t);var a=o("2b0e"),s=function(){var e=this,t=e.$createElement,o=e._self._c||t;return o("v-app",{staticClass:"djeym",style:"width:"+e.widthMap+";height:"+e.heightMap+";",attrs:{id:"djeym-app"}},[o("v-sheet",{staticClass:"overflow-hidden",staticStyle:{position:"relative"},attrs:{tile:"",width:e.widthMap,height:e.heightMap}},[e.createPanel?o("v-navigation-drawer",{attrs:{app:"","hide-overlay":"",absolute:"",temporary:"",permanent:e.isPermanentPanel,width:e.widthPanel,height:e.heightMap,src:e.imgBgPanel},model:{value:e.openPanel,callback:function(t){e.openPanel=t},expression:"openPanel"}},[o("v-container",{staticClass:"pa-0",style:"min-height: 100%; background-color: "+e.tinting+";",attrs:{fluid:""}},[o("v-card-actions",{staticClass:"pb-0"},[o("v-spacer"),o("v-btn",{attrs:{icon:"",ripple:e.effectRipple},on:{click:function(t){t.stopPropagation(),e.isPermanentPanel=!1,e.openPanel=!1}}},[o("v-icon",{attrs:{color:e.colorControls}},[e._v("mdi-close")])],1)],1),o("v-tabs",{style:e.isHideTabs?"position: relative; top: -45px; z-index: -10;":"",attrs:{height:"42",centered:"","show-arrows":"","center-active":"","background-color":"transparent",color:e.colorControls},model:{value:e.tab,callback:function(t){e.tab=t},expression:"tab"}},[o("v-tabs-slider"),e._l(e.сategoryIcons,(function(t,a){return[e.isShowTab(a)?o("v-tab",{key:"button-tab-"+a,attrs:{href:"#tab-"+a,ripple:e.effectRipple}},[o("v-icon",[e._v(e._s(t))])],1):e._e()]}))],2),o("v-tabs-items",{style:"background-color: transparent;"+(e.isHideTabs?"top: -45px;":""),model:{value:e.tab,callback:function(t){e.tab=t},expression:"tab"}},e._l(3,(function(t,a){return o("v-tab-item",{key:"item-"+t,attrs:{value:"tab-"+a}},[0===a?[e.hideGeoTypes?e._e():o("v-card-title",{staticClass:"title pt-3 pb-0 px-3",class:e.centerGeoTypes?"justify-center":""},[e._v(e._s(e.geoTypeNameMarker?e.geoTypeNameMarker:e.$t("message.1")))])]:e._e(),1===a?[e.hideGeoTypes?e._e():o("v-card-title",{staticClass:"title pt-3 pb-0 px-3",class:e.centerGeoTypes?"justify-center":""},[e._v(e._s(e.geoTypeNameRoute?e.geoTypeNameRoute:e.$t("message.2")))])]:e._e(),2===a?[e.hideGeoTypes?e._e():o("v-card-title",{staticClass:"title pt-3 pb-0 px-3",class:e.centerGeoTypes?"justify-center":""},[e._v(e._s(e.geoTypeNameTerritory?e.geoTypeNameTerritory:e.$t("message.3")))])]:e._e(),e.hideGeoTypes?e._e():o("v-divider"),e.hideGeoTypes?o("div",{staticClass:"pt-4"}):e._e(),o("v-container",{staticClass:"pt-0",attrs:{fluid:""}},e._l(e.nextTwoFilters(a),(function(t,a,s){return o("v-list",{key:"filters-"+a,staticClass:"pa-0",staticStyle:{"background-color":"transparent"},attrs:{shaped:"shaped"===e.controlsShape,rounded:"rounded"===e.controlsShape,flat:"flat"===e.controlsShape,dense:""}},[0===s?[o("v-card-subtitle",{staticClass:"font-italic px-0 pb-1",class:s?"pt-1":"pt-0"},[e._v(e._s(t.length&&!e.hideGroupNames?e.groupNameCategories?e.groupNameCategories:e.$t("message.4"):""))])]:e._e(),1===s?[o("v-card-subtitle",{staticClass:"font-italic px-0 pb-1",class:s?"pt-1":"pt-0"},[e._v(e._s(t.length&&!e.hideGroupNames?e.groupNameSubcategories?e.groupNameSubcategories:e.$t("message.5"):""))])]:e._e(),o("v-list-item-group",{attrs:{multiple:(s+1)%2==0||e.multiple},model:{value:e.models[a],callback:function(t){e.$set(e.models,a,t)},expression:"models[modelKey]"}},e._l(t,(function(t){return o("v-list-item",{key:"control-"+t.id,staticClass:"mb-1",attrs:{color:t.color,ripple:e.effectRipple},on:{click:function(o){t.isActive=!t.isActive,e.filtering({id:t.id,modelKey:a})}}},[o("v-list-item-icon",{staticClass:"my-auto mr-3"},[o("v-icon",{attrs:{color:t.color}},[e._v(e._s(t.icon))])],1),o("v-list-item-content",[o("v-list-item-title",{staticClass:"subtitle-2 djeym-white-space-normal"},[e._v(e._s(t.title))])],1)],1)})),1)],2)})),1)],2)})),1)],1)],1):e._e(),e.createForm?o("v-navigation-drawer",{attrs:{app:"",right:"",absolute:"",temporary:"","hide-overlay":"",permanent:e.isPermanentForm,height:e.heightMap},model:{value:e.openForm,callback:function(t){e.openForm=t},expression:"openForm"}},[o("v-container",{staticClass:"pt-0",attrs:{fluid:""}},[o("v-row",[o("v-col",{staticClass:"pt-3 pb-5",attrs:{cols:"12"}},[o("v-select",{attrs:{items:e.customMarkerCategoryList,"item-text":"title","item-value":"id",label:e.$t("message.4"),dense:"","prepend-icon":"mdi-select-marker",color:e.colorControls,"item-color":e.colorControls,"hide-details":""},model:{value:e.updateCustomMarkerCategory,callback:function(t){e.updateCustomMarkerCategory=t},expression:"updateCustomMarkerCategory"}})],1)],1),e.customMarkerSubcategoryList.length?o("v-row",[o("v-col",{staticClass:"pt-3 pb-5",attrs:{cols:"12"}},[o("v-select",{attrs:{items:e.customMarkerSubcategoryList,"item-text":"title","item-value":"id",label:e.$t("message.5"),dense:"",multiple:"","prepend-icon":"mdi-select-multiple-marker",color:e.colorControls,"item-color":e.colorControls,"hide-details":""},model:{value:e.updateCustomMarkerSubcategories,callback:function(t){e.updateCustomMarkerSubcategories=t},expression:"updateCustomMarkerSubcategories"}})],1)],1):e._e(),o("v-row",[o("v-col",{staticClass:"pt-0 pb-0",attrs:{cols:"12"}},[o("v-file-input",{attrs:{label:e.$t("message.7"),"prepend-icon":"mdi-camera-outline",accept:"image/jpeg",hint:e.$t("message.15"),"persistent-hint":"",clearable:"",color:e.colorControls},on:{change:e.optimizeImage}})],1)],1),o("v-row",[o("v-col",{staticClass:"py-0",attrs:{cols:"12"}},[o("v-text-field",{attrs:{label:e.$t("message.6"),color:e.colorControls,counter:"60","prepend-icon":"mdi-map-marker-circle",rules:e.titleRules(),clearable:""},model:{value:e.customMarkerTitle,callback:function(t){e.customMarkerTitle=t},expression:"customMarkerTitle"}})],1)],1),o("v-row",[o("v-col",{staticClass:"py-0",attrs:{cols:"12"}},[o("v-textarea",{attrs:{counter:"300",label:e.$t("message.8"),rows:"1","prepend-icon":"mdi-tooltip-text-outline",color:e.colorControls,rules:e.descriptionRules(),clearable:""},model:{value:e.customMarkerDescription,callback:function(t){e.customMarkerDescription=t},expression:"customMarkerDescription"}})],1)],1),o("v-row",[o("v-col",{staticClass:"py-0",attrs:{cols:"12"}},[o("v-text-field",{attrs:{label:e.$t("message.11"),color:e.colorControls,maxlength:"254","prepend-icon":"mdi-email-outline",clearable:"",rules:e.emailRules()},model:{value:e.customMarkerEmail,callback:function(t){e.customMarkerEmail=t},expression:"customMarkerEmail"}})],1)],1),o("v-row",[o("v-col",{attrs:{cols:"9"}},[o("v-btn",{attrs:{tile:"",depressed:"",block:"",color:"green darken-1",ripple:e.effectRipple},on:{click:function(t){return e.saveCustomMarker()}}},[o("span",{staticClass:"white--text"},[e._v(e._s(e.$t("message.10")))])])],1),o("v-col",{staticClass:"pl-0",attrs:{cols:"3"}},[o("v-btn",{attrs:{tile:"",depressed:"",block:"",color:"red darken-1",ripple:e.effectRipple},on:{click:function(t){return e.closeCustomMarker()}}},[o("v-icon",{attrs:{color:"white"}},[e._v("mdi-close")])],1)],1)],1)],1)],1):e._e(),o("v-container",{staticClass:"pa-0 fill-height",attrs:{fluid:""}},[o("div",{staticClass:"djeym-ymap",attrs:{fluid:"",id:"djeymYMapsID"}})]),o("v-snackbar",{attrs:{top:"","multi-line":"",vertical:"",timeout:0,color:e.$vuetify.theme.dark?"#323232":"white"},model:{value:e.showAlert,callback:function(t){e.showAlert=t},expression:"showAlert"}},[o("v-btn",{staticClass:"mt-0 pb-0",attrs:{icon:"",color:"white",ripple:e.effectRipple},on:{click:function(t){e.showAlert=!e.showAlert}}},[o("v-icon",{attrs:{color:"pink"}},[e._v("mdi-close")])],1),o("span",{class:e.$vuetify.theme.dark?"grey--text text--lighten-5":"grey--text text--darken-4",domProps:{innerHTML:e._s("<table width='294' class='djeym-pos-relative djeym-pos-top--8'><tr><td>"+e.textAlert+"</td></tr></table>")}})],1),o("v-overlay",{attrs:{"z-index":"10000",value:e.progressBar}},[o("v-progress-circular",{attrs:{indeterminate:"",size:"64"}})],1),o("canvas",{staticClass:"djeym-hide",attrs:{id:"djeym-canvas"}})],1)],1)},l=[],i=(o("219c"),{name:"App",data:()=>({enableAjax:!0,createPanel:!1,createForm:!1,themeType:"light",colorControls:"#FFA000",colorButtonsText:"#212121",widthMap:"0",heightMap:"0",openPanel:!1,tmpOpenPanel:!1,isPermanentPanel:!1,widthPanel:380,imgBgPanel:void 0,tinting:"#00000000",tab:null,multiple:!0,isHideTabs:!1,centerGeoTypes:!1,hideGeoTypes:!1,geoTypeNameMarker:"",geoTypeNameRoute:"",geoTypeNameTerritory:"",hideGroupNames:!1,groupNameCategories:"",groupNameSubcategories:"",controlsShape:"shaped",effectRipple:!0,openForm:!1,isPermanentForm:!1,customMarkerTitle:null,customMarkerDescription:null,customMarkerEmail:null,customMarkerCategory:null,customMarkerSubcategories:[],customMarkerCategoryList:[],customMarkerSubcategoryList:[],customMarkerCoordinates:[0,0],customPlacemark:null,progressBar:!1,optimizedImgBlob:null,currImg:null,"сategoryIcons":["mdi-map-marker","mdi-routes","mdi-beach"],transCategoryNames:[1,2,3],transGroupNames:[4,5],filters:{a:[],b:[],c:[],d:[],e:[],f:[]},models:{a:[],b:[],c:[],d:[],e:[],f:[]},Map:null,mapCursor:null,isActiveHeatmap:!1,globalHeatmap:null,globalHeatPoints:null,globalObjMngPlacemark:null,globalObjMngPolyline:null,globalObjMngPolygon:null,showAlert:!1,textAlert:""}),computed:{updateCustomMarkerCategory:{get(){return this.customMarkerCategory},set(e){this.customMarkerCategory=e}},updateCustomMarkerSubcategories:{get(){return this.customMarkerSubcategories},set(e){this.customMarkerSubcategories=e}}},methods:{optimizeImage(e){if(window.File&&window.FileReader&&window.FileList&&window.Blob){if(this.currImg=e,null!==e){const t=966,o=t,a=t,s=new FileReader,l=new Image;let i,r;s.onload=()=>{l.onload=()=>{i=l.width,r=l.height,i>r?i>o&&(r=Math.floor(r*(o/i)),i=o):r>a&&(i=Math.floor(i*a/r),r=a);const t=window.document.getElementById("djeym-canvas"),s=t.getContext("2d");s.clearRect(0,0,t.width,t.height),t.width=i,t.height=r,s.drawImage(l,0,0,i,r);const n=t.toDataURL(e.type),c=e=>{const t=atob(e.split(",")[1]),o=new ArrayBuffer(t.length),a=new Uint8Array(o);for(let s=0;s<t.length;s++)a[s]=t.charCodeAt(s);return new Blob([o],{type:"image/jpeg"})};this.optimizedImgBlob=c(n)},l.src=s.result},s.readAsDataURL(e)}}else this.alertSnackbarShow(this.$t("message.18"))},titleRules(){return[e=>!!e||this.$t("message.12"),e=>String(e).length<=60||this.$t("message.13")]},descriptionRules(){return[e=>!!e||this.$t("message.12"),e=>String(e).length<=300||this.$t("message.14")]},emailRules(){return[e=>!!e||this.$t("message.12")]},isShowTab(e){const t=this.filters;switch(e){case 0:return t.a.length>0||t.b.length>0;case 1:return t.c.length>0||t.d.length>0;case 2:return t.e.length>0||t.f.length>0}},nextTwoFilters(e){const t=this.filters;let o={};return Object.keys(t).slice(e*=2,e+2).map(e=>({[e]:t[e]})).forEach(e=>{o[Object.keys(e)[0]]=Object.values(e)[0]}),o},generalFilter(e){const t=[],o=[];let a=0;this.filters[e.filterName1].forEach(e=>{e.isActive&&t.push(e.id)}),this.filters[e.filterName2].forEach(e=>{e.isActive&&o.push(e.id)}),a=o.length,a>0?this[e.globalObjMngName].setFilter(e=>{let s=e.properties.subCategoryIDs;return t.includes(e.properties.categoryID)&&s.filter(e=>o.includes(e)).length===a}):this[e.globalObjMngName].setFilter(e=>t.includes(e.properties.categoryID))},filtering(e){const t=e.id,o=e.modelKey;if(!this.multiple&&["a","c","e","g","i"].includes(o)){let e=this.filters[o];for(let o=0,a=e.length;o<a;o++){let a=e[o];if(a.isActive&&a.id!==t){a.isActive=!1;break}}}switch(o){case"a":case"b":this.generalFilter({filterName1:"a",filterName2:"b",globalObjMngName:"globalObjMngPlacemark"});break;case"c":case"d":this.generalFilter({filterName1:"c",filterName2:"d",globalObjMngName:"globalObjMngPolyline"});break;case"e":case"f":this.generalFilter({filterName1:"e",filterName2:"f",globalObjMngName:"globalObjMngPolygon"});break}},refreshVisibilityGeoObjects(){const e=[{filterName1:"a",filterName2:"b",globalObjMngName:"globalObjMngPlacemark"},{filterName1:"c",filterName2:"d",globalObjMngName:"globalObjMngPolyline"},{filterName1:"e",filterName2:"f",globalObjMngName:"globalObjMngPolygon"}];e.forEach(e=>{this.generalFilter({filterName1:e.filterName1,filterName2:e.filterName2,globalObjMngName:e.globalObjMngName})})},ajaxErrorMessage(e,t,o,a){const s=`${t} , ${o}`,l="ERROR<br>Request Failed -> "+s;let i="";void 0!==e.responseJSON&&void 0!==e.responseJSON.detail&&(i=e.responseJSON.detail),window.console.log(l),this.textAlert=`${l}<br>Hint -> ${a}<br>${i}`,this.showAlert=!0},uploadSettings(){this.enableAjax&&window.$.getJSON("/djeym/ajax-upload-settings-front/",{mapID:window.djeymMapID}).done(e=>{this.themeType=e.themeType,this.$vuetify.theme.dark={light:!1,dark:!0}[this.themeType],this.colorControls=e.colorControls,this.colorButtonsText=e.colorButtonsText,this.widthPanel=e.widthPanel,this.сategoryIcons=e.сategoryIcons,this.imgBgPanel=e.imgBgPanel||void 0,this.tinting=e.tinting,this.centerGeoTypes=e.centerGeoTypes,this.hideGeoTypes=e.hideGeoTypes,this.geoTypeNameMarker=e.geoTypeNameMarker,this.geoTypeNameRoute=e.geoTypeNameRoute,this.geoTypeNameTerritory=e.geoTypeNameTerritory,this.hideGroupNames=e.hideGroupNames,this.groupNameCategories=e.groupNameCategories,this.groupNameSubcategories=e.groupNameSubcategories,this.controlsShape=e.controlsShape,this.effectRipple=e.effectRipple;const t=e.multiple,o=e.filters;this.multiple=t,this.filters=o;const a=this.models;let s=!0;for(let i in o)s&&(a[i]=t?Array.from(Array(o[i].length).keys()):0),s=!s;this.customMarkerCategoryList=o.a.map(e=>({id:e.id,title:e.title})),this.customMarkerSubcategoryList=o.b.map(e=>({id:e.id,title:e.title}));const l=[o.a.length>0||o.b.length>0,o.c.length>0||o.d.length>0,o.e.length>0||o.f.length>0];this.isHideTabs=l.filter(e=>e).length<2,e.openPanel?this.tmpOpenPanel=!0:(this.isPermanentPanel=!1,this.tmpOpenPanel=!1),this.isActiveHeatmap=e.heatmap.isActive,window.djeymYMaps.ready().then(()=>this.initMap(e))}).fail((e,t,o)=>{const a="Ajax - Upload all settings.";this.ajaxErrorMessage(e,t,o,a)})},closeCustomMarker(){this.Map.balloon.close(),this.Map.geoObjects.remove(this.customPlacemark),this.customMarkerTitle=null,this.customMarkerDescription=null,this.customMarkerEmail=null,this.updateCustomMarkerCategory=null,this.updateCustomMarkerSubcategories=[],this.customMarkerCoordinates=[0,0],this.customPlacemark=null,this.isPermanentForm=!1,this.openForm=!1,this.progressBar=!1,this.optimizedImgBlob=null,this.currImg=null,this.showAlert=!1,this.mapCursor.remove()},saveCustomMarker(){this.Map.balloon.close(),this.showAlert=!1;const e=this.customMarkerTitle,t=this.customMarkerDescription,o=this.customMarkerEmail,a=this.updateCustomMarkerCategory;if(!a)return this.textAlert=`${this.$t("message.4")} --\x3e ${this.$t("message.12")}`,void(this.showAlert=!0);if(null===e)return this.textAlert=`${this.$t("message.6")} --\x3e ${this.$t("message.12")}`,void(this.showAlert=!0);if(null===t)return this.textAlert=`${this.$t("message.8")} --\x3e ${this.$t("message.12")}`,void(this.showAlert=!0);if(null===o)return this.textAlert=`${this.$t("message.11")} --\x3e ${this.$t("message.12")}`,void(this.showAlert=!0);this.progressBar=!0;const s=new FormData;s.append("ymap",window.djeymMapID),s.append("csrfmiddlewaretoken",window.djeymCSRFToken),s.append("header",e),s.append("body",t),s.append("footer",""),s.append("category",+a),s.append("user_email",o),s.append("icon_slug","djeym-marker-default"),s.append("coordinates",JSON.stringify(this.customMarkerCoordinates)),s.append("active",!1),s.append("is_user_marker",!0),null!==this.currImg?s.append("user_image",this.optimizedImgBlob,"pic.jpg"):s.append("user_image",null),this.updateCustomMarkerSubcategories.forEach(e=>{s.append("subcategories",+e)}),window.$.ajax({type:"POST",url:"/djeym/ajax-save-cusotm-marker/",data:s,cache:!1,processData:!1,contentType:!1,dataType:"json"}).done(()=>{setTimeout(()=>{this.closeCustomMarker(),this.textAlert=this.$t("message.9"),this.showAlert=!0},1e3)}).fail((e,t,o)=>{setTimeout(()=>{this.progressBar=!1;const a="Ajax - Save custom marker.";this.ajaxErrorMessage(e,t,o,a)},1e3)})},addPlacemarkTypeObjects(e){this.globalObjMngPlacemark.add({type:"FeatureCollection",features:e})},addHeatPoints(e){this.isActiveHeatmap&&(this.globalHeatPoints.features.push(e),this.globalHeatmap.setData(this.globalHeatPoints))},addPolylineTypeObjects(e){this.globalObjMngPolyline.add({type:"FeatureCollection",features:e})},addPolygonTypeObjects(e){this.globalObjMngPolygon.add({type:"FeatureCollection",features:e})},initMap(e){const t=e.currentTile,o=null!==t?new Function("return "+t.randomTileUrl):null,a=e.activeControls.includes("typeSelector"),s=e.activeControls.filter(e=>"typeSelector"!==e),l=e.isRoundTheme,i=e.heatmap;let r=[];const n=()=>{r[3]=setTimeout(()=>{const e=document.getElementById("djeymLoadIndicator");if(null===e)return;e.style.display="block";const t=window.$("ymaps:regex(class, .*-balloon__content) img");let o=!1,a=0;if(0===t.length?o=!0:(t.each((e,t)=>{t.complete&&a++}),a===t.length&&(o=!0)),o){window.$(".djeymUpdateInfoPreset").each((e,t)=>{window.$(t).trigger("click")});const e=document.getElementById("djeymModalLock");null!==e&&(r[1]=setTimeout(()=>{r[0]=setTimeout(()=>{e.remove()},600),e.style.opacity=0},200))}else r[2]=setTimeout(()=>{n()},100)},500)},c=window.djeymYMaps.templateLayoutFactory.createClass('<div class="djeym-pos-relative djeym-fill-hight"><div id="djeymModalLock"><div id="djeymLoadIndicator"></div></div><div class="djeym_ballon_header">{{ properties.balloonContentHeader|raw }}</div><div class="djeym_ballon_body">{{ properties.balloonContentBody|raw }}</div><div class="djeym_ballon_footer">{{ properties.balloonContentFooter|raw }}</div></div>'),d=window.djeymYMaps.templateLayoutFactory.createClass('<div class="djeym_layout_cluster_icon"><span style="background-color:'+e.colorBackgroundCountObjects+";color:"+e.textColorCountObjects+';">$[properties.geoObjects.length]</span></div>'),p=new window.djeymYMaps.Map("djeymYMapsID",{center:e.mapCenter,zoom:e.mapZoom,type:null,controls:l?[]:s},{minZoom:null!==t?t.minZoom:0,maxZoom:null!==t?t.maxZoom:23,geoObjectHasBalloon:!0,hasHint:!1,geoObjectBalloonMinWidth:322,geoObjectBalloonMaxWidth:342,geoObjectBalloonMinHeight:window.djeymBalloonMinHeight,geoObjectBalloonPanelMaxMapArea:0,geoObjectOpenBalloonOnClick:!0});if(this.Map=p,a){let a;if(l?a=new window.djeymYMaps.control.TypeSelector({options:{layout:"round#listBoxLayout",size:"small",float:"none",position:{bottom:"40px",left:"10px"}}}):(a=new window.djeymYMaps.control.TypeSelector,a.options.set("panoramasItemMode",e.isPanorama?"ifMercator":"off")),a.addMapType("yandex#map",2),a.addMapType("yandex#satellite",3),a.addMapType("yandex#hybrid",4),null!==t){let e=function(){let e=new window.djeymYMaps.Layer(o(),{projection:window.djeymYMaps.projection.sphericalMercator});return e.getCopyrights=function(){return window.djeymYMaps.vow.resolve(t.copyrights)},e.getZoomRange=function(){return window.djeymYMaps.vow.resolve([t.minZoom,t.maxZoom])},e};window.djeymYMaps.layer.storage.add("tile#aerial",e);let s=new window.djeymYMaps.MapType(t.title,["tile#aerial"]);window.djeymYMaps.mapType.storage.add("tile#current",s),a.addMapType("tile#current",1),p.controls.add(a),p.setType("tile#current",{checkZoomRange:!0})}else p.controls.add(a),p.setType("yandex#map")}else null!==t?(p.layers.add(new window.djeymYMaps.Layer(o(),{projection:window.djeymYMaps.projection.sphericalMercator})),p.copyrights.add(t.copyrights)):p.setType("yandex#map");if(l){if(s.includes("geolocationControl")){let e=new window.djeymYMaps.control.GeolocationControl({options:{layout:"round#buttonLayout",floatIndex:4,size:"small"}});p.controls.add(e)}if(s.includes("routeButtonControl")){let e=new window.djeymYMaps.control.Button({data:{iconType:"routes"},options:{layout:"round#buttonLayout",floatIndex:2,size:"small"}});p.controls.add(e),p.controls.add("routePanelControl",{visible:!1,showHeader:!0,floatIndex:1,float:"left",top:"auto",right:"auto",bottom:"auto",left:"auto"});let t=p.controls.get("routePanelControl");e.events.add("press",()=>{t.options.get("visible")?(t.options.set("visible",!1),t.routePanel.state.set("fromEnabled",!1)):(t.options.set("visible",!0),t.routePanel.state.set("fromEnabled",!0))})}if(s.includes("searchControl")){let e=new window.djeymYMaps.control.SearchControl({options:{size:"small",float:"none",position:{top:-40}}}),t=new window.djeymYMaps.control.Button({data:{iconType:"loupe"},options:{layout:"round#buttonLayout",size:"small",floatIndex:3,selectOnClick:!1,float:"left"}});t.events.add("press",()=>{window.$("ymaps:regex(class, ymaps-.+-float-button-icon_icon_magnifier)").trigger("click")}),p.controls.add(e),p.controls.add(t)}if(s.includes("trafficControl")){let e=new window.djeymYMaps.control.TrafficControl({options:{visible:!1}}),t=new window.djeymYMaps.control.Button({data:{iconType:"traffic"},options:{layout:"round#buttonLayout",floatIndex:1,size:"small",float:"right"}});t.events.add("press",()=>{e.isTrafficShown()?e.hideTraffic():e.showTraffic()}),p.controls.add(e),p.controls.add(t)}if(s.includes("fullscreenControl")){let e=new window.djeymYMaps.control.FullscreenControl({data:{iconType:"expand"},options:{layout:"round#buttonLayout",size:"small",floatIndex:2,selectOnClick:!1}});e.events.add("press",()=>{e.isSelected()?p.container.exitFullscreen():p.container.enterFullscreen()}),p.container.events.add("fullscreenenter",()=>{e.data.set({iconType:"collapse"}),e.select()}),p.container.events.add("fullscreenexit",()=>{e.data.set({iconType:"expand"}),e.deselect()}),p.controls.add(e)}if(s.includes("zoomControl")){let e=new window.djeymYMaps.control.ZoomControl({options:{layout:"round#zoomLayout",size:"small"}});p.controls.add(e)}if(s.includes("rulerControl")){let e=new window.djeymYMaps.control.RulerControl({options:{layout:"round#rulerLayout",size:"small",position:{bottom:"40px",right:"10px"}}});p.controls.add(e)}}else s.includes("searchControl")&&e.isSearchByOrganization&&p.controls.get("searchControl").options.set("provider","yandex#search");i.isActive&&window.djeymYMaps.modules.require(["Heatmap"],e=>{this.globalHeatPoints={type:"FeatureCollection",features:[]},this.globalHeatmap=new e(this.globalHeatPoints,{radius:i.radius,dissipating:i.dissipating,opacity:i.opacity,intensityOfMidpoint:i.intensity,gradient:{.1:i.gradient.color1,.2:i.gradient.color2,.7:i.gradient.color3,1:i.gradient.color4}}),this.globalHeatmap.setMap(p)}),p.events.add("balloonopen",()=>{for(let e=0,t=r.length;e<t;e++)clearTimeout(r[e]);n()}),window.$(document).on("click","ymaps:regex(class, .*-cluster-tabs__menu-item.*), ymaps:regex(class, .*-cluster-carousel__pager-item.*), ymaps:regex(class, .*-cluster-carousel__nav.*)",e=>{e.stopPropagation();for(let t=0,o=r.length;t<o;t++)clearTimeout(r[t]);n()});const m={geoObjectHasBalloon:!0,geoObjectHasHint:!1,geoObjectBalloonMinWidth:322,geoObjectBalloonMaxWidth:342,geoObjectBalloonMinHeight:window.djeymBalloonMinHeight,geoObjectBalloonPanelMaxMapArea:0,geoObjectBalloonContentLayout:c,geoObjectOpenBalloonOnClick:!1},u=parseInt(Math.min.apply(null,e.cluster.size)/2),g={clusterize:e.isClusterize,clusterHasBalloon:!0,clusterHasHint:!1,clusterIconContentLayout:e.isIconContentLayout?d:null,clusterBalloonItemContentLayout:c,clusterDisableClickZoom:!0,clusterOpenBalloonOnClick:!1,showInAlphabeticalOrder:!1,clusterBalloonPanelMaxMapArea:0,clusterMaxZoom:p.options.get("maxZoom"),gridSize:128,margin:u+2,clusterBalloonContentLayout:e.balloonContentLayout,clusterIcons:[{href:e.cluster.url,size:e.cluster.size,offset:e.cluster.offset,shape:{type:"Circle",coordinates:[0,0],radius:u}}]};Object.assign(g,m),this.globalObjMngPlacemark=new window.djeymYMaps.ObjectManager(g),this.globalObjMngPolyline=new window.djeymYMaps.ObjectManager(m),this.globalObjMngPolygon=new window.djeymYMaps.ObjectManager(m);const h=e=>(e.properties.balloonContentHeader="",e.properties.balloonContentBody="",e.properties.balloonContentFooter="",e);this.globalObjMngPlacemark.clusters.events.add("click",e=>{p.balloon.close(!0);const t=e.get("objectId"),o=this.globalObjMngPlacemark.clusters.getById(t),a=o.properties.geoObjects,s=a.length,l=[];for(let i=0;i<s;i++)l.push(a[i].properties.id);for(let i=0;i<s;i++)this.globalObjMngPlacemark.clusters.balloon.setData(h(a[i]));setTimeout(()=>{this.globalObjMngPlacemark.clusters.balloon.open(t)},100),window.$.get("/djeym/ajax-balloon-content/",{ids:JSON.stringify(l),objType:"Point",isPresets:"True"}).done((function(e){for(let t,o,l=0;l<s;l++)t=a[l],o=e[t.properties.id],t.properties.balloonContentHeader=o.header,t.properties.balloonContentBody=o.body,t.properties.balloonContentFooter=o.footer;window.$("ymaps:regex(class, .*-cluster-tabs__menu-item.*)").eq(0).trigger("click")})).fail((e,t,o)=>{const a=`${t} , ${o}`,s="ERROR<br>Request Failed -> "+a,l="Ajax - Uploading content for Cluster.";window.console.log(s),this.textAlert=`${s} <br>Hint -> ${l}`,this.showAlert=!0})});const b=e=>{p.balloon.close(!0);const t=e.geometry.type;setTimeout(()=>{"Point"===t?this.globalObjMngPlacemark.objects.balloon.open(e.id):"LineString"===t?this.globalObjMngPolyline.objects.balloon.open(e.id):"Polygon"===t&&this.globalObjMngPolygon.objects.balloon.open(e.id)},100),window.$.get("/djeym/ajax-balloon-content/",{objID:e.properties.id,objType:t,isPresets:"True"}).done(o=>{e.properties.balloonContentHeader=o.header,e.properties.balloonContentBody=o.body,e.properties.balloonContentFooter=o.footer,"Point"===t?this.globalObjMngPlacemark.objects.balloon.setData(e):"LineString"===t?this.globalObjMngPolyline.objects.balloon.setData(e):"Polygon"===t&&this.globalObjMngPolygon.objects.balloon.setData(e)}).fail((e,t,o)=>{const a=`${t} , ${o}`,s="ERROR<br>Request Failed -> "+a,l="Ajax - Uploading content for geo objects.";window.console.log(s),this.textAlert=`${s} <br>Hint -> ${l}`,this.showAlert=!0})};this.globalObjMngPlacemark.objects.events.add("click",e=>{const t=e.get("objectId");let o=this.globalObjMngPlacemark.objects.getById(t);o=h(o),b(o)}),this.globalObjMngPolyline.objects.events.add("click",e=>{const t=e.get("objectId");let o=this.globalObjMngPolyline.objects.getById(t);o=h(o),b(o)}),this.globalObjMngPolygon.objects.events.add("click",e=>{const t=e.get("objectId");let o=this.globalObjMngPolygon.objects.getById(t);o=h(o),b(o)}),p.geoObjects.add(this.globalObjMngPlacemark),p.geoObjects.add(this.globalObjMngPolyline),p.geoObjects.add(this.globalObjMngPolygon),this.refreshVisibilityGeoObjects();const y=e=>{window.$.getJSON("/map/ajax-upload-placemarks/",{filters:filters,offset:e}).done(t=>{setTimeout(()=>{t.length>0?(this.addPlacemarkTypeObjects(t),e+=1e3,y(e)):setTimeout(()=>f(0),0)},0)}).fail((e,t,o)=>{const a=`${t} , ${o}`,s="ERROR<br>Request Failed -> "+a,l="Ajax - Load Placemarks.";window.console.log(s),this.textAlert=`${s} <br>Hint -> ${l}`,this.showAlert=!0})};y(0);const f=e=>{window.$.getJSON("/djeym/ajax-upload-heat-points/",{mapID:window.djeymMapID,offset:e}).done(t=>{setTimeout(()=>{t.length>0?(this.addHeatPoints(t),e+=1e3,f(e)):setTimeout(()=>w(0),0)},0)}).fail((e,t,o)=>{const a=`${t} , ${o}`,s="ERROR<br>Request Failed -> "+a,l="Ajax - Loading Thermal points.";window.console.log(s),this.textAlert=`${s} <br>Hint -> ${l}`,this.showAlert=!0})},w=e=>{window.$.getJSON("/djeym/ajax-upload-polylines/",{mapID:window.djeymMapID,offset:e}).done(t=>{setTimeout(()=>{t.length>0?(this.addPolylineTypeObjects(t),e+=500,w(e)):setTimeout(()=>j(0),0)},0)}).fail((e,t,o)=>{const a=`${t} , ${o}`,s="ERROR<br>Request Failed -> "+a,l="Ajax - Load Polylines.";window.console.log(s),this.textAlert=`${s} <br>Hint -> ${l}`,this.showAlert=!0})},j=e=>{window.$.getJSON("/djeym/ajax-upload-polygons/",{mapID:window.djeymMapID,offset:e}).done(t=>{setTimeout(()=>{t.length>0?(this.addPolygonTypeObjects(t),e+=500,j(e)):setTimeout(()=>{window.$("#djeym-open-panel").length&&(this.createPanel=!0),window.$("#djeym-add-marker").length&&(this.createForm=!0),setTimeout(()=>{this.tmpOpenPanel&&(this.openPanel=!0,this.isPermanentPanel=!0),window.$(document).on("click","#djeym-open-panel",()=>{this.openPanel=!0,this.isPermanentPanel=!0}),window.$(document).on("click","#djeym-add-marker",()=>{this.openForm||(this.Map.balloon.close(),this.mapCursor=this.Map.cursors.push("arrow"),this.isPermanentPanel=!1,this.openPanel=!1,this.openForm=!0,this.isPermanentForm=!0,this.customPlacemark=new window.djeymYMaps.Placemark(p.getCenter(),{hintContent:"",balloonContent:""},{iconLayout:"default#image",iconImageHref:"/static/djeym/img/center.svg",iconImageSize:[32,60],iconImageOffset:[-16,-60],draggable:!0}),this.customPlacemark.events.add("drag",e=>{const t=e.get("target").geometry.getCoordinates();this.customMarkerCoordinates=t}),this.Map.geoObjects.add(this.customPlacemark),this.textAlert=this.$t("message.17"),this.showAlert=!0)}),this.Map.events.add("click",e=>{if(null!==this.customPlacemark){const t=e.get("coords");this.customPlacemark.geometry.setCoordinates(t),this.customMarkerCoordinates=t}})},void 0!==this.imgBgPanel?1e3:0)},0)},0)}).fail((e,t,o)=>{const a=`${t} , ${o}`,s="ERROR<br>Request Failed -> "+a,l="Ajax - Load Polygons.";window.console.log(s),this.textAlert=`${s} <br>Hint -> ${l}`,this.showAlert=!0})}}},created(){this.widthMap=window.djeymWidthMap,this.heightMap=window.djeymHeightMap,void 0!==window.djeymMapID&&window.$(".djeym-button-bar").show(),this.uploadSettings()}}),r=i,n=(o("2f99"),o("2877")),c=o("6544"),d=o.n(c),p=o("7496"),m=o("8336"),u=o("99d9"),g=o("62ad"),h=o("a523"),b=o("ce7e"),y=o("23a7"),f=o("132d"),w=o("8860"),j=o("da13"),M=o("5d23"),v=o("1baa"),k=o("34c3"),C=o("f774"),P=o("a797"),O=o("490a"),T=o("0fd9"),x=o("b974"),$=o("8dd9"),I=o("2db4"),_=o("2fa4"),A=o("71a3"),S=o("c671"),N=o("fe57"),R=o("aac8"),B=o("9a96"),F=o("8654"),L=o("a844"),H=Object(n["a"])(r,s,l,!1,null,"3c9b3361",null),D=H.exports;d()(H,{VApp:p["a"],VBtn:m["a"],VCardActions:u["a"],VCardSubtitle:u["b"],VCardTitle:u["c"],VCol:g["a"],VContainer:h["a"],VDivider:b["a"],VFileInput:y["a"],VIcon:f["a"],VList:w["a"],VListItem:j["a"],VListItemContent:M["a"],VListItemGroup:v["a"],VListItemIcon:k["a"],VListItemTitle:M["b"],VNavigationDrawer:C["a"],VOverlay:P["a"],VProgressCircular:O["a"],VRow:T["a"],VSelect:x["a"],VSheet:$["a"],VSnackbar:I["a"],VSpacer:_["a"],VTab:A["a"],VTabItem:S["a"],VTabs:N["a"],VTabsItems:R["a"],VTabsSlider:B["a"],VTextField:F["a"],VTextarea:L["a"]});var V=o("f309");a["a"].use(V["a"]);const Y={icons:{iconfont:"mdi"}};var z=new V["a"](Y),E=o("a925");a["a"].use(E["a"]);const G={en:{message:{1:"Places",2:"Routes",3:"Territories",4:"Categories",5:"Subcategories",6:"Title",7:"Upload image",8:"Short description",9:"The marker will appear on the map after successful moderation.",10:"Save",11:"Your E-mail",12:"Required",13:"Max 60 characters",14:"Max 300 characters",15:"Only JPG files",16:"Close",17:"1. Click on the map in the right place.<br>2. If necessary, move the marker.",18:"The File APIs are not fully supported in this browser.",19:"Invalid address"}},ru:{message:{1:"Места",2:"Маршруты",3:"Территории",4:"Категории",5:"Подкатегории",6:"Название",7:"Загрузите изображение",8:"Краткое описание",9:"Маркер появится на карте после успешной модерации.",10:"Сохранить",11:"Ваш E-mail",12:"Обязательно",13:"Макс. 60 символов",14:"Макс. 300 символов",15:"Только JPG файлы",16:"Закрыть",17:"1. Кликните по карте в нужном месте.<br>2. Если необходимо, переместите маркер.",18:"Файловые API не полностью поддерживаются в этом браузере.",19:"Некорректный адрес"}}};let J=window.djeymLanguageCode.slice(0,2);Object.keys(G).includes(J)||(J="en");const Z={locale:J,messages:G};var q=new E["a"](Z);o("744d");a["a"].config.productionTip=!1,new a["a"]({vuetify:z,i18n:q,render:e=>e(D)}).$mount("#djeym-app")},"744d":function(e,t,o){},af57:function(e,t,o){}});
//# sourceMappingURL=app.56b637c0.js.map