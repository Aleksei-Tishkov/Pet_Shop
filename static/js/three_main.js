import * as THREE from 'three';
import { ObjectLoader } from 'node_modules/three';

const container = document.getElementById( 'canvas' );
const elem = document.getElementById( 'canvas_father' );
elem.appendChild( container );

const camera = new THREE.PerspectiveCamera( 70, elem.offsetWidth / elem.offsetHeight, 0.01, 10 );
camera.position.z = 0.5;

const scene = new THREE.Scene();

const loader = new ObjectLoader;
loader.load('models/Ribba_Nemo__corona.obj', function ( object ) {

scene.add( object );
});

const renderer = new THREE.WebGLRenderer( { alpha: true, antialias: true } );
renderer.setSize( elem.offsetWidth, elem.offsetHeight );
container.appendChild( renderer.domElement );
renderer.setAnimationLoop( animation );

// animation

function animation( time ) {

	mesh.rotation.x = time / 2000;
	mesh.rotation.y = time / 1000;

	renderer.render( scene, camera );

}