import * as THREE from 'three';
import { RoomEnvironment } from 'three/examples/jsm/environments/RoomEnvironment.js';
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader";
import { DRACOLoader } from "three/examples/jsm/loaders/DRACOLoader";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";

const scene = new THREE.Scene();

const environment = new RoomEnvironment();

const camera = new THREE.PerspectiveCamera( 35, window.innerWidth / window.innerHeight, 0.1, 1000 );
camera.position.z = 5;

const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild(renderer.domElement);

const loader = new GLTFLoader();

const dracoLoader = new DRACOLoader();
dracoLoader.setDecoderPath("/draco/");

loader.setDRACOLoader( dracoLoader );
loader.load("/models/room.glb", function (gltf) {

scene.add(gltf.scene);
console.log(gltf.scene);
});


const controls = new OrbitControls( camera, renderer.domElement );
controls.target.set( 0, 0.5, 0 );
controls.update();
controls.enablePan = false;
controls.enableDamping = true;

const light = new THREE.DirectionalLight("#ffffff", 3);
light.castShadow = true;
light.shadow.camera.far = 20;
light.shadow.mapSize.set(1024,1024);
light.shadow.normalBias = 0.05;
light.position.set(1.5, 7, 3);
scene.add(light);

renderer.render( scene, camera );