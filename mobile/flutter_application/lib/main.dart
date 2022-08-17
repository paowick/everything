import 'package:flutter/material.dart';
import 'package:lab/simpletab.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      initialRoute: '/',
      routes: {
        '/': (context) => MyHomePage(),
        '/second': (context) => SecondScreen(),
        '/simpletab': (context) => SimpleTap(),
      },
    );
  }
}

class MyHomePage extends StatelessWidget {
  const MyHomePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Hello World'),
      ),
      backgroundColor: Colors.blueAccent,
      //body=============================================================
      body: Container(
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                ElevatedButton(
                  child: Text('SimpleTap'),
                  onPressed: () {
                    Navigator.pushNamed(context, '/simpletab');
                  },
                ),
                ElevatedButton(
                  child: Text('two'),
                  onPressed: () {
                    //Navigator.pushNamed(context, '/second');
                    Navigator.pushReplacementNamed(context, '/second');
                  },
                ),
                Text('Two'),
              ],
            )
          ],
        ),
      ),
    );
  }
}

class SecondScreen extends StatefulWidget {
  const SecondScreen({Key? key}) : super(key: key);

  @override
  State<SecondScreen> createState() => _SecondScreenState();
}

class _SecondScreenState extends State<SecondScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Second Page'),
      ),
      body: ElevatedButton(
        child: Text('one'),
        onPressed: () {
          Navigator.popAndPushNamed(context, '/');
        },
      ),
    );
  }
}

class GreenFrong extends StatelessWidget {
  const GreenFrong({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.blue,
    );
  }
}

class YellowBird extends StatefulWidget {
  const YellowBird({Key? key}) : super(key: key);

  @override
  State<YellowBird> createState() => _YellowBirdState();
}

class _YellowBirdState extends State<YellowBird> {
  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.yellow,
    );
  }
}
