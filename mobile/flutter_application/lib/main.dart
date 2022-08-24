import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);
  static const String _title = 'Flutter Code Sample';

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: _title,
      home: MyStatefulWidget(),
    );
  }
}

class MyStatefulWidget extends StatefulWidget {
  const MyStatefulWidget({Key? key}) : super(key: key);
  @override
  State<MyStatefulWidget> createState() => _MyStatefulWidgetState();
}

class _MyStatefulWidgetState extends State<MyStatefulWidget> {
  int _selectedIndex = 0;
  static const TextStyle optionStyle =
      TextStyle(fontSize: 30, fontWeight: FontWeight.bold);
  static const List<Widget> _widgetOpions = <Widget>[
    Text(
      'index 0l Home',
      style: optionStyle,
    ),
    Text(
      'index 02 Business',
      style: optionStyle,
    ),
    Text(
      'index 03 School',
      style: optionStyle,
    ),
    _myListView(),
  ];
  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('BottomNavigationBar Sample'),
      ),
      body: Center(
        child: _widgetOpions.elementAt(_selectedIndex),
      ),
      bottomNavigationBar: BottomNavigationBar(
        type: BottomNavigationBarType.shifting,
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(icon: Icon(Icons.home), label: 'home'),
          BottomNavigationBarItem(
              icon: Icon(Icons.business), label: 'business'),
          BottomNavigationBarItem(icon: Icon(Icons.school), label: 'school'),
          BottomNavigationBarItem(icon: Icon(Icons.ads_click), label: "คำคม")
        ],
        currentIndex: _selectedIndex,
        selectedItemColor: Colors.teal[800],
        unselectedItemColor: Colors.teal[200],
        onTap: _onItemTapped,
      ),
    );
  }
}

class _myListView extends StatelessWidget {
  const _myListView({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ListView(
      children: [
        ListTile(
          leading: CircleAvatar(child: Icon(Icons.local_hospital)),
          title: Text('Hospital'),
          onTap: () {
            print('Hospital');
          },
        ),
        ListTile(
          leading: const CircleAvatar(
            foregroundImage: NetworkImage(
                'https://www.techhub.in.th/wp-content/uploads/2021/05/577280151-1.jpg'),
          ),
          title: Text('Police Station'),
          onTap: () {
            print('Police Station');
          },
        ),
        ListTile(
          leading: CircleAvatar(child: Icon(Icons.star)),
          title: Text('Attraction'),
          onTap: () {
            print('Attraction');
          },
        ),
      ],
    );
  }
}
